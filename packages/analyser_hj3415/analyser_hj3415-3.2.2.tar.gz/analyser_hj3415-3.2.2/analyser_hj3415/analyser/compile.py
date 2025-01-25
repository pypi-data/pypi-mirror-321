import os
from collections import OrderedDict
from typing import Union

from db_hj3415 import myredis,mymongo
from utils_hj3415 import tools, setup_logger

from analyser_hj3415.analyser import tsa, eval, MIs

mylogger = setup_logger(__name__,'WARNING')
expire_time = tools.to_int(os.getenv('DEFAULT_EXPIRE_TIME_H', 48)) * 3600

class MICompile:
    def __init__(self, mi_type: str):
        assert mi_type in MIs.keys(), f"Invalid MI type ({MIs.keys()})"
        self._mi_type = mi_type
        self.prophet = tsa.MIProphet(mi_type)
        self.lstm = tsa.MILSTM(mi_type)

    @property
    def mi_type(self) -> str:
        return self._mi_type

    @mi_type.setter
    def mi_type(self, mi_type: str):
        assert mi_type in MIs.keys(), f"Invalid MI type ({MIs.keys()})"
        self._mi_type = mi_type
        self.prophet.mi_type = mi_type
        self.lstm.mi_type = mi_type

    def get(self, refresh=False) -> dict:
        """
        특정 MI(Market Index) 타입 데이터를 컴파일하고 반환합니다.
        데이터를 Redis 캐시에서 가져오거나, 새로 생성하여 캐시에 저장합니다.

        Args:
            refresh (bool, optional):
                - True: 캐시를 무시하고 데이터를 새로 생성하여 저장.
                - False: 캐시된 데이터를 가져오며, 없을 경우 새로 생성.
                Defaults to False.

        Returns:
            dict: MI 데이터를 포함하는 딕셔너리로 반환하며, 다음의 키를 포함합니다:
                - 'name' (str): MI 타입 이름.
                - 'trading_action' (str): 예측된 매매 신호 ('buy', 'sell', 'hold').
                - 'prophet_score' (float): Prophet 모델의 예측 점수.
                - 'lstm_grade' (float): LSTM 모델의 최종 예측 점수.
                - 'is_lstm_up' (bool): LSTM 모델이 상승 신호를 나타내는지 여부.
                - 'prophet_html' (str): prophet_html,
                - 'lstm_html' (str): lstm_html ,
        Example:
            {
                'name': 'example_mi',
                'trading_action': 'buy',
                'prophet_score': 0.88,
                'lstm_grade': 0.92,
                'is_lstm_up': True,
                'prophet_html': prophet_html...,
                'lstm_html': lstm_html...,
            }
        """
        print(f"{self.mi_type}의 compiling을 시작합니다.")
        redis_name = self.mi_type + '_mi_compile'
        print(
            f"redisname: '{redis_name}' / refresh : {refresh} / expire_time : {expire_time / 3600}h")

        def fetch_mi_compile() -> dict:
            print(f"{self.mi_type}")
            trading_action, prophet_score = self.prophet.scoring()
            prophet_html = self.prophet.export()
            self.lstm.initializing()
            _, lstm_grade = self.lstm.get_final_predictions(refresh=refresh, num=5)
            is_lstm_up = self.lstm.is_lstm_up()
            lstm_html= self.lstm.export()

            return {
                'name': self.mi_type,
                'trading_action': trading_action,
                'prophet_score': prophet_score,
                'lstm_grade': lstm_grade,
                'is_lstm_up': is_lstm_up,
                'prophet_html': prophet_html,
                'lstm_html': lstm_html,
            }

        data_dict = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_mi_compile, timer=expire_time)
        return data_dict

    @staticmethod
    def analyser_lstm_all_mi(refresh: bool):
        mi_lstm = tsa.MILSTM('wti')
        print(f"*** LSTM prediction redis cashing Market Index items ***")
        for mi_type in MIs.keys():
            mi_lstm.mi_type = mi_type
            print(f"{mi_lstm.mi_type}")
            mi_lstm.initializing()
            mi_lstm.get_final_predictions(refresh=refresh, num=5)


class CorpCompile:
    def __init__(self, code: str, expect_earn=0.06):
        assert tools.is_6digit(code), f'Invalid value : {code}'
        self._code = code
        self.name = mymongo.Corps.get_name(code)
        self.red = eval.Red(code, expect_earn)
        self.mil = eval.Mil(code)
        self.prophet = tsa.CorpProphet(code)

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, code: str):
        assert tools.is_6digit(code), f'Invalid value : {code}'
        mylogger.info(f'change code : {self.code} -> {code}')
        self._code = code
        self.name = mymongo.Corps.get_name(code)
        self.red.code = code
        self.mil.code = code
        self.prophet.code = code

    def get(self, refresh=False) -> dict:
        """
        특정 기업 데이터를 컴파일하여 반환합니다.
        데이터를 Redis 캐시에서 가져오거나, 새로 생성하여 캐시에 저장합니다.

        Args:
            refresh (bool, optional):
                - True: 캐시를 무시하고 데이터를 새로 생성하여 저장.
                - False: 캐시된 데이터를 가져오며, 없을 경우 새로 생성.
                Defaults to False.

        Returns:
            dict: 기업 데이터를 포함하는 딕셔너리로 반환되며, 다음의 키를 포함합니다:
                - 'name' (str): 기업 이름.
                - 'red_score' (float): 기업의 Red Score (위험 점수).
                - '이익지표' (float): 기업의 이익 지표.
                - '주주수익률' (float): 주주 수익률.
                - 'trading_action' (str): 예측된 매매 신호 ('buy', 'sell', 'hold').
                - 'prophet_score' (float): Prophet 모델의 예측 점수.
                - 'prophet_html' (str): prophet_html,

        Example:
            {
                'name': 'Samsung Electronics',
                'red_score': 0.85,
                '이익지표': 0.75,
                '주주수익률': 0.10,
                'trading_action': 'buy',
                'prophet_score': 0.92,
                'prophet_html': prophet_html...,
            }
        """
        print(f"{self.code}/{self.name}의 compiling을 시작합니다.")
        redis_name = self.code + '_corp_compile'
        print(
            f"redisname: '{redis_name}' / refresh : {refresh} / expire_time : {expire_time/3600}h")

        def fetch_corp_compile() -> dict:
            mylogger.info("Red score 계산중..")
            red_score = self.red.get(verbose=False).score

            mylogger.info("Mil data 계산중..")
            mil_data = self.mil.get(verbose=False)

            mylogger.info("\tProphet 최근 데이터 조회중..")
            trading_action, prophet_score = self.prophet.scoring()
            prophet_html = self.prophet.export()

            return {
                'name': self.name,
                'red_score': red_score,
                '이익지표': mil_data.이익지표,
                '주주수익률': mil_data.주주수익률,
                'trading_action': trading_action,
                'prophet_score': prophet_score,
                'prophet_html': prophet_html,
            }
        data_dict = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_corp_compile, timer=expire_time)
        return data_dict

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

        def fetch_ranking() -> dict:
            data = {}
            c = CorpCompile('005930')
            for code in myredis.Corps.list_all_codes():
                try:
                    c.code = code
                except ValueError:
                    mylogger.error(f'prophet ranking error : {code}')
                    continue
                scores= c.get(refresh=refresh)
                print(f'{code} compiled : {scores}')
                data[code] = scores
            return data

        data_dict = myredis.Base.fetch_and_cache_data(redis_name, refresh, fetch_ranking, timer=expire_time)

        # prophet_score를 기준으로 정렬
        ranking = OrderedDict(sorted(data_dict.items(), key=lambda x: x[1]['prophet_score'], reverse=True))

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
            corp_lstm.initializing()
            corp_lstm.get_final_predictions(refresh=refresh, num=5)


