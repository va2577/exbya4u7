import numpy as np
import pandas as pd
import requests

def get(symbol='USDJPY', timeframe='daily', count=240):
    if timeframe == '4h':
        timeframe = '1h'
        count = count * 4
    header = {
        # 'Cookie': 'bar_range=daily; AWSALB=CiYmPetsLHGniQN4PjE/PBb/hfzytcDA2InF2HaJ0yfA2erFcvDfkRg3iijINbXuJKe972Bji5+V1QfM53wH3ZwE0i2HyII7eghztmY/ykV+UOdMJ4fFQTqsh2j4; _mintame_session=cC9TWkVqWGpCT2RVRUpacVY1TVQyTFZLaGdxSldkRGVFbjFGMnNnYU1uMiszTUozSlltOVFES3hBa254TG8rNTBEbURpcVdBbmlDZndaSjB1Zzc0MFZjOXU5WW1GS3dkV2JkQ3NSMnJoYzJIQXNmQi9IRjdkOExzeEtMc3ozTmFZdVRUd2lCNkx4UmRNWHAzbXhCd2xRPT0tLTdyK2o5RFdsNm1YaThwQUdsc3ZBVVE9PQ%3D%3D--b5ca03902a17bd78a2778b95fdfd3278f61c5194',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'fx.minkabu.jp',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ja-jp',
        'Referer': f'https://fx.minkabu.jp/pair/{symbol}',
        'Connection': 'keep-alive',
    }
    params = {
        'count': count + 40,
    }
    with requests.Session() as s:
        r1 = s.get(f'https://fx.minkabu.jp/pair/{symbol}')
        r1.raise_for_status()
        s.headers.update(header)
        r2 = s.get(f'https://fx.minkabu.jp/api/v2/bar/{symbol}/{timeframe}.json', params=params)
        r2.raise_for_status()
        return r2.json()

def to_json(d, timeframe='daily'):
    df = pd.DataFrame(d, columns=['datetime', 'open', 'high', 'low', 'close'], dtype=np.float64)
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df = df.set_index('datetime')
    if timeframe == '4h':
        ohlc = {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last'
        }
        df = df.resample('4H', closed='left', label='left').agg(ohlc)
    df = df.dropna()
    df = df.tail(240)
    df = df.reset_index()
    values = df.to_json(orient='values')
    # with open(f'static/{timeframe}.json', 'w') as f:
    #     f.write(values)
    return values
