import json
import numpy as np
import pandas as pd
import requests

def step_timeframe(timeframe='daily'):
    step = {
        'daily': 'P1D',
        '4h': 'PT1H',
        '1h': 'PT1H',
        '15m': 'PT15M',
    }
    timeframe2 = {
        'daily': 'P1Y',
        '4h': 'D10',
        '1h': 'D10',
        '15m': 'D5',
    }
    return step[timeframe], timeframe2[timeframe]

def query_string(symbol='EURUSD', timeframe='daily'):
    step, timeframe2 = step_timeframe(timeframe)
    d = {
        'Step': step,
        'TimeFrame': timeframe2,
        'StartDate': 1572739200000,
        'EndDate': 1572739200000,
        'EntitlementToken': '57494d5ed7ad44af85bc59a51dd87c90',
        'IncludeMockTick': True,
        'FilterNullSlots': False,
        'FilterClosedPoints': True,
        'IncludeClosedSlots': False,
        'IncludeOfficialClose': True,
        'InjectOpen': False,
        'ShowPreMarket': False,
        'ShowAfterHours': False,
        'UseExtendedTimeFrame': True,
        'WantPriorClose': False,
        'IncludeCurrentQuotes': False,
        'ResetTodaysAfterHoursPercentChange': False,
        'Series': [{
            'Key': f'CURRENCY/US/XTUP/{symbol}',
            'Dialect': 'Charting',
            'Kind': 'Ticker',
            'SeriesId': 's1',
            'DataTypes': ['Open', 'High', 'Low', 'Last']
        }]
    }
    return {
        'json': json.dumps(d, separators=(',', ':')),
        'ckey': '57494d5ed7',
    }

def get(symbol='EURUSD', timeframe='daily'):
    url = 'https://api.wsj.net/api/michelangelo/timeseries/history'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://quotes.wsj.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'api.wsj.net',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ja-jp',
        'Referer': f'https://quotes.wsj.com/fx/{symbol}/advanced-chart',
        'Connection': 'keep-alive',
        'Dylan2010.EntitlementToken': '57494d5ed7ad44af85bc59a51dd87c90',
    }
    params = query_string(symbol, timeframe)
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    return r.json()

def to_json(d, timeframe='daily'):
    data = d['Series'][0]['DataPoints']
    index = pd.to_datetime(d['TimeInfo']['Ticks'], unit='ms').rename('Ticks')
    # columns = d['Series'][0]['DesiredDataPoints']
    columns = ['open', 'high', 'low', 'close']
    df = pd.DataFrame(data=data, index=index, columns=columns)
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
