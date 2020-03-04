import datetime
import numpy as np
import pandas as pd
import requests

def periods(n=1):
    today = datetime.datetime.today()
    period2 = today.timestamp()
    time = {
        'hour': 0,
        'minute': 0,
        'second': 0,
        'microsecond': 0,
    }
    period1 = (today - pd.offsets.BusinessDay(n)).replace(**time).timestamp()
    return int(period1), int(period2)

def get(symbol='EURUSD', timeframe='daily'):
    d = {
        'USDJPY': 'JPY=X',
        'EURJPY': 'EURJPY=X',
        'EURUSD': 'EURUSD=X',
    }
    d2 = {
        'daily': '1d',
        '4h': '1h',
        '1h': '1h',
        '15m': '15m',
    }
    d3 = {
        'daily': 270,
        '4h': 40,
        '1h': 11,
        '15m': 3,
    }
    symbol2 = d[symbol]
    interval = d2[timeframe]
    period1, period2 = periods(d3[timeframe])
    header = {
        'Accept': '*/*',
        'Origin': 'https://finance.yahoo.com',
        # 'Cookie': 'PRF=t%3DJPY%253DX; thamba=1; B=5ei4fk9erqori&b=3&s=uk',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'query1.finance.yahoo.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ja-jp',
        # 'Referer': 'https://finance.yahoo.com/chart/JPY%3DX',
        'Connection': 'keep-alive',
    }
    params = {
        # 'symbol': 'JPY=X',
        'symbol': symbol2,
        # 'period1': '1571411763',
        # 'period2': '1572707763',
        'period1': period1,
        'period2': period2,
        # 'period': '5d',
        # 'interval': '15m',
        'interval': interval,
        'includePrePost': 'true',
        'events': 'div|split|earn',
        'lang': 'en-US',
        'region': 'US',
        'crumb': 'WxNG8rXM15r',
        'corsDomain': 'finance.yahoo.com',
    }
    with requests.Session() as s:
        r1 = s.get(f'https://finance.yahoo.com/chart/{symbol}')
        r1.raise_for_status()
        s.headers.update(header)
        r2 = s.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}', params=params)
        r2.raise_for_status()
        return r2.json()

def to_json(d, timeframe='daily'):
    data = {
        'open': d['chart']['result'][0]['indicators']['quote'][0]['open'],
        'high': d['chart']['result'][0]['indicators']['quote'][0]['high'],
        'low': d['chart']['result'][0]['indicators']['quote'][0]['low'],
        'close': d['chart']['result'][0]['indicators']['quote'][0]['close'],
    }
    index = pd.to_datetime(d['chart']['result'][0]['timestamp'], unit='s').rename('timestamp')
    df = pd.DataFrame(data=data, index=index)
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
