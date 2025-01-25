import os
from collections import OrderedDict
from typing import Union
from dataclasses import dataclass

from db_hj3415 import myredis
from utils_hj3415 import tools, setup_logger

from analyser_hj3415.analyser import tsa, eval, MIs

mylogger = setup_logger(__name__,'WARNING')
expire_time = tools.to_int(os.getenv('DEFAULT_EXPIRE_TIME_H', 48)) * 3600


@dataclass
class MICompileData:
    mi_type: str

    prophet_data: tsa.ProphetData
    lstm_grade: tsa.LSTMGrade

    is_lstm_up: bool = False
    is_prophet_up: bool = False

    lstm_html: str = ''
    prophet_html: str = ''


class MICompile:
    def __init__(self, mi_type: str):
        assert mi_type in MIs._fields, f"Invalid MI type ({MIs._fields})"
        self._mi_type = mi_type

    @property
    def mi_type(self) -> str:
        return self._mi_type

    @mi_type.setter
    def mi_type(self, mi_type: str):
        assert mi_type in MIs._fields, f"Invalid MI type ({MIs._fields})"
        self._mi_type = mi_type

    def get(self, refresh=False) -> MICompileData:
        print(f"{self.mi_type}의 compiling을 시작합니다.")
        redis_name = self.mi_type + '_mi_compile'
        print(
            f"redisname: '{redis_name}' / refresh : {refresh} / expire_time : {expire_time / 3600}h")

        def fetch_mi_compile_data() -> MICompileData:
            prophet = tsa.MIProphet(self.mi_type)
            lstm = tsa.MILSTM(self.mi_type)

            data = MICompileData(
                mi_type=self.mi_type,
                prophet_data=prophet.generate_data(refresh=refresh),
                lstm_grade=lstm.get_final_predictions(refresh=refresh)[1],
            )
            data.is_lstm_up = lstm.is_lstm_up()
            data.is_prophet_up = prophet.is_prophet_up(refresh=False)
            data.lstm_html = lstm.export(refresh=False)
            data.prophet_html = prophet.export()
            return data

        mi_compile_data = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_mi_compile_data, timer=expire_time)
        return mi_compile_data

    @staticmethod
    def analyser_lstm_all_mi(refresh: bool):
        mi_lstm = tsa.MILSTM('WTI')
        print(f"*** LSTM prediction redis cashing Market Index items ***")
        for mi_type in MIs._fields:
            mi_lstm.mi_type = mi_type
            print(f"{mi_lstm.mi_type}")
            mi_lstm.initializing()
            mi_lstm.get_final_predictions(refresh=refresh, num=5)


@dataclass
class CorpCompileData:
    code: str
    name: str

    red_data: eval.RedData
    mil_data: eval.MilData

    prophet_data: tsa.ProphetData
    lstm_grade: tsa.LSTMGrade

    is_lstm_up: bool = False
    is_prophet_up: bool = False

    lstm_html: str = ''
    prophet_html: str = ''


class CorpCompile:
    def __init__(self, code: str, expect_earn=0.06):
        assert tools.is_6digit(code), f'Invalid value : {code}'
        self._code = code
        self.expect_earn = expect_earn

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, code: str):
        assert tools.is_6digit(code), f'Invalid value : {code}'
        mylogger.info(f'change code : {self.code} -> {code}')
        self._code = code

    def get(self, refresh=False) -> dict:
        print(f"{self.code}의 compiling을 시작합니다.")
        redis_name = self.code + '_corp_compile'
        print(
            f"redisname: '{redis_name}' / refresh : {refresh} / expire_time : {expire_time/3600}h")

        def fetch_corp_compile_data() -> CorpCompileData:
            prophet = tsa.CorpProphet(self.code)
            lstm = tsa.CorpLSTM(self.code)

            data = CorpCompileData(
                code=self.code,
                name=myredis.Corps(self.code,'c101').get_name(data_from='mongo'),
                red_data=eval.Red(self.code, self.expect_earn).get(refresh=refresh, verbose=False),
                mil_data=eval.Mil(self.code).get(refresh=refresh, verbose=False),
                prophet_data=prophet.generate_data(refresh=refresh),
                lstm_grade=lstm.get_final_predictions(refresh=refresh)[1],
            )

            data.is_lstm_up = lstm.is_lstm_up()
            data.is_prophet_up = prophet.is_prophet_up(refresh=False)
            data.lstm_html = lstm.export(refresh=False)
            data.prophet_html = prophet.export()
            return data

        corp_compile_data = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_corp_compile_data, timer=expire_time)
        return corp_compile_data

    @staticmethod
    def red_ranking(expect_earn: float = 0.06, refresh=False) -> OrderedDict:
        # 이전 expect earn 과 비교하여 다르거나 없으면 강제 refresh 설정
        redis_name = 'red_ranking_prev_expect_earn'
        pee = tools.to_float(myredis.Base.get_value(redis_name))
        if pee != expect_earn:
            # expect earn의 이전 계산값이 없거나 이전 값과 다르면 새로 계산
            mylogger.warning(
                f"expect earn : {expect_earn} / prev expect earn : {pee} 두 값이 달라 refresh = True"
            )
            myredis.Base.set_value(redis_name, str(expect_earn))
            refresh = True

        print("**** Start red_ranking... ****")
        redis_name = 'red_ranking'
        print(
            f"redisname: '{redis_name}' / expect_earn: {expect_earn} / refresh : {refresh} / expire_time : {expire_time / 3600}h")

        def fetch_ranking(refresh_in: bool) -> dict:
            data = {}
            red = eval.Red(code='005930', expect_earn=expect_earn)
            for i, code in enumerate(myredis.Corps.list_all_codes()):
                red.code = code
                red_score = red.get(refresh=refresh_in, verbose=False).score
                if red_score > 0:
                    data[code] = red_score
                    print(f"{i}: {red} - {red_score}")
            return data

        data_dict = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_ranking, refresh, timer=expire_time)

        return OrderedDict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))

    @staticmethod
    def prophet_ranking(refresh=False, top: Union[int, str]='all') -> OrderedDict:

        print("**** Start Compiling scores and sorting... ****")
        redis_name = 'prophet_ranking'

        print(
            f"redisname: '{redis_name}' / refresh : {refresh} / expire_time : {expire_time/3600}h")

        def fetch_prophet_ranking() -> dict:
            data = {}
            c = tsa.CorpProphet('005930')
            for code in myredis.Corps.list_all_codes():
                try:
                    c.code = code
                except ValueError:
                    mylogger.error(f'prophet ranking error : {code}')
                    continue
                score= c.generate_data(refresh=refresh).score
                print(f'{code} compiled : {score}')
                data[code] = score
            return data

        data_dict = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_prophet_ranking, timer=expire_time)

        # prophet_score를 기준으로 정렬
        ranking = OrderedDict(sorted(data_dict.items(), key=lambda x: x[1], reverse=True))

        if top == 'all':
            return ranking
        else:
            if isinstance(top, int):
                return OrderedDict(list(ranking.items())[:top])
            else:
                raise ValueError("top 인자는 'all' 이나 int형 이어야 합니다.")

    @staticmethod
    def analyse_lstm_topn(refresh: bool, top=40):
        ranking_topn = CorpCompile.prophet_ranking(refresh=False, top=top)
        mylogger.info(ranking_topn)
        corp_lstm = tsa.CorpLSTM('005930')
        print(f"*** LSTM prediction redis cashing top{top} items ***")
        for i, (code, _) in enumerate(ranking_topn.items()):
            corp_lstm.code = code
            print(f"{i + 1}. {corp_lstm.code}/{corp_lstm.name}")
            corp_lstm.get_final_predictions(refresh=refresh, num=5)
