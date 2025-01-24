import argparse
import pprint

from utils_hj3415 import tools
from analyser_hj3415.analyser import eval, tsa, compile
from db_hj3415 import myredis, mymongo


def analyser_manager():
    from analyser_hj3415.analyser.tsa import MIs
    parser = argparse.ArgumentParser(description="Analyser Commands")
    type_subparsers = parser.add_subparsers(dest='type', help='분석 타입')

    # prophet 명령어 서브파서
    prophet_parser = type_subparsers.add_parser('prophet', help='MyProphet 타입')
    prophet_subparser = prophet_parser.add_subparsers(dest='command', help='prophet 관련된 명령')
    # prophet - ranking 파서
    ranking_parser = prophet_subparser.add_parser('ranking', help='prophet 랭킹 책정 및 레디스 저장')
    ranking_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')
    # prophet - score 파서
    prophet_get_parser = prophet_subparser.add_parser('score', help='prophet score 계산')
    prophet_get_parser.add_argument('target', type=str, help=f'종목코드 or {list(MIs.keys())}')
    prophet_get_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')

    # lstm 명령어 서브파서
    lstm_parser = type_subparsers.add_parser('lstm', help='MyLSTM 타입')
    lstm_subparser = lstm_parser.add_subparsers(dest='command', help='lstm 관련된 명령')
    # lstm - caching 파서
    caching_parser = lstm_subparser.add_parser('caching', help='lstm 랭킹 책정 및 레디스 저장')
    caching_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')
    caching_parser.add_argument('-t', '--top', type=int, help='prophet ranking 몇위까지 작업을 할지')
    # lstm - predict 파서
    lstm_get_parser = lstm_subparser.add_parser('predict', help='lstm get final prediction 시행')
    lstm_get_parser.add_argument('target', type=str, help=f'종목코드 or {list(MIs.keys())}')
    lstm_get_parser.add_argument('-n', '--num', type=int, default=5, help='ensemble training 횟수 설정')
    lstm_get_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')

    # red 명령어 서브파서
    red_parser = type_subparsers.add_parser('red', help='red 타입')
    red_subparser = red_parser.add_subparsers(dest='command', help='red 관련된 명령')
    # red - ranking 파서
    ranking_parser = red_subparser.add_parser('ranking', help='red 랭킹 책정 및 레디스 저장')
    ranking_parser.add_argument('-e', '--expect_earn', type=float, help='기대수익률 (실수 값 입력)')
    ranking_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')
    # red - get 파서
    red_get_parser = red_subparser.add_parser('get', help='red get 책정 및 레디스 저장')
    red_get_parser.add_argument('code', type=str, help='종목코드 or all')
    red_get_parser.add_argument('-e', '--expect_earn', type=float, help='기대수익률 (실수 값 입력)')
    red_get_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')

    # mil 명령어 서브파서
    mil_parser = type_subparsers.add_parser('mil', help='millennial 타입')
    mil_subparser = mil_parser.add_subparsers(dest='command', help='mil 관련된 명령')
    # mil - get 파서
    mil_get_parser = mil_subparser.add_parser('get', help='mil get 책정 및 레디스 저장')
    mil_get_parser.add_argument('code', type=str, help='종목코드 or all')
    mil_get_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')

    # blue 명령어 서브파서
    blue_parser = type_subparsers.add_parser('blue', help='Blue 타입')
    blue_subparser = blue_parser.add_subparsers(dest='command', help='blue 관련된 명령')
    # blue - get 파서
    blue_get_parser = blue_subparser.add_parser('get', help='blue get 책정 및 레디스 저장')
    blue_get_parser.add_argument('code', type=str, help='종목코드 or all')
    blue_get_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')

    # growth 명령어 서브파서
    growth_parser = type_subparsers.add_parser('growth', help='Growth 타입')
    growth_subparser = growth_parser.add_subparsers(dest='command', help='growth 관련된 명령')
    # growth - get 파서
    growth_get_parser = growth_subparser.add_parser('get', help='growth get 책정 및 레디스 저장')
    growth_get_parser.add_argument('code', type=str, help='종목코드 or all')
    growth_get_parser.add_argument('-r', '--refresh', action='store_true', help='래디스 캐시를 사용하지 않고 강제로 재계산 할지')

    args = parser.parse_args()

    if args.type == 'red':
        if args.command == 'get':
            if args.expect_earn is None:
                red = eval.Red('005930')
            else:
                red = eval.Red('005930', expect_earn=args.expect_earn)
            if args.code == 'all':

                print("**** Red - all codes ****")
                for i, code in enumerate(myredis.Corps.list_all_codes()):
                    red.code = code
                    print(f"*** {i} / {red} ***")
                    pprint.pprint(red.get(args.refresh, verbose=False))
            else:
                assert tools.is_6digit(args.code), "code 인자는 6자리 숫자이어야 합니다."
                # 저장된 기대수익률을 불러서 임시저장
                red.code = args.code
                print(f"*** Red - {red} ***")
                pprint.pprint(red.get(args.refresh))
            # mymongo.Logs.save('cli','INFO', f'run >> analyser red get {args.code}')

        elif args.command == 'ranking':
            mymongo.Logs.save('cli', 'INFO', 'run >> analyser red ranking')
            try:
                if args.expect_earn is None:
                    result = compile.Compile.red_ranking(refresh=args.refresh)
                else:
                    result = compile.Compile.red_ranking(expect_earn=args.expect_earn, refresh=args.refresh)
                print(result)
            except Exception as e:
                print(e)
                mymongo.Logs.save('cli', 'ERROR', f'analyser red ranking 실행중 에러 - {e}')

    elif args.type == 'mil':
        if args.command == 'get':
            mymongo.Logs.save('cli', 'INFO', f'run >> analyser mil get {args.code}')
            try:
                if args.code == 'all':
                    mil = eval.Mil('005930')
                    print("**** Mil - all codes ****")
                    for i, code in enumerate(myredis.Corps.list_all_codes()):
                        mil.code = code
                        print(f"*** {i} / {mil} ***")
                        pprint.pprint(mil.get(args.refresh, verbose=False))
                else:
                    assert tools.is_6digit(args.code), "code 인자는 6자리 숫자이어야 합니다."
                    mil = eval.Mil(args.code)
                    print(f"*** Mil - {mil} ***")
                    pprint.pprint(mil.get(args.refresh))
            except Exception as e:
                print(e)
                mymongo.Logs.save('cli', 'ERROR', f'analyser mil get {args.code} 실행중 에러 - {e}')

    elif args.type == 'blue':
        if args.command == 'get':
            mymongo.Logs.save('cli', 'INFO', f'run >> analyser blue get {args.code}')
            try:
                if args.code == 'all':
                    blue = eval.Blue('005930')
                    print("**** Blue - all codes ****")
                    for i, code in enumerate(myredis.Corps.list_all_codes()):
                        blue.code = code
                        print(f"*** {i} / {blue} ***")
                        pprint.pprint(blue.get(args.refresh, verbose=False))
                else:
                    assert tools.is_6digit(args.code), "code 인자는 6자리 숫자이어야 합니다."
                    blue = eval.Blue(args.code)
                    print(f"*** Blue - {blue} ***")
                    pprint.pprint(blue.get(args.refresh))
            except Exception as e:
                print(e)
                mymongo.Logs.save('cli', 'ERROR', f'analyser blue get {args.code} 실행중 에러 - {e}')

    elif args.type == 'growth':
        if args.command == 'get':
            mymongo.Logs.save('cli', 'INFO', f'run >> analyser growth get {args.code}')
            try:
                if args.code == 'all':
                    growth = eval.Growth('005930')
                    print("**** Growth - all codes ****")
                    for i, code in enumerate(myredis.Corps.list_all_codes()):
                        growth.code = code
                        print(f"*** {i} / {growth} ***")
                        pprint.pprint(growth.get(args.refresh, verbose=False))
                else:
                    assert tools.is_6digit(args.code), "code 인자는 6자리 숫자이어야 합니다."
                    growth = eval.Growth(args.code)
                    print(f"*** growth - {growth} ***")
                    pprint.pprint(growth.get(args.refresh))
            except Exception as e:
                print(e)
                mymongo.Logs.save('cli', 'ERROR', f'analyser growth get {args.code} 실행중 에러 - {e}')

    elif args.type == 'prophet':
        if args.command == 'ranking':
            mymongo.Logs.save('cli', 'INFO', 'run >> analyser prophet ranking')
            try:
                result = compile.Compile.prophet_ranking(refresh=args.refresh)
                print(result)
            except Exception as e:
                print(e)
                mymongo.Logs.save('cli', 'ERROR', f'analyser prophet ranking 실행중 에러 - {e}')
        elif args.command == 'score':
            if args.target in MIs.keys():
                myprophet = tsa.MIProphet(args.target)
            elif tools.is_6digit(args.target):
                myprophet = tsa.CorpProphet(args.target)
            else:
                raise Exception("Invalid target")
            print(myprophet.scoring())
            # mymongo.Logs.save('cli','INFO', f'run >> analyser prophet get {args.target}')

    elif args.type == 'lstm':
        if args.command == 'caching':
            mymongo.Logs.save('cli', 'INFO', f'run >> analyser lstm caching')
            try:
                if args.top:
                    compile.Compile.analyse_lstm_topn(refresh=args.refresh, top=args.top)
                else:
                    compile.Compile.analyse_lstm_topn(refresh=args.refresh)
            except Exception as e:
                print(e)
                mymongo.Logs.save('cli','ERROR', f'analyser lstm caching 실행중 에러 - {e}')
        elif args.command == 'predict':
            if args.target in MIs.keys():
                mylstm = tsa.MILSTM(args.target)
            elif tools.is_6digit(args.target):
                mylstm = tsa.CorpLSTM(args.target)
            else:
                raise Exception("Invalid target")
            mylstm.initializing()
            future_data, grade = mylstm.get_final_predictions(refresh=args.refresh, num=args.num)
            print(future_data)
            print(grade)
            # mymongo.Logs.save('cli','INFO', f'run >> analyser lstm get {args.target}')
    else:
        parser.print_help()
