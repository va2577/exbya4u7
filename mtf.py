import json
import numpy as np
import pandas as pd
import requests
from flask import Flask, jsonify, render_template, request, send_from_directory
import minkabu
import wsj
import yahoo

app = Flask(__name__)

@app.route('/data.json', methods=['GET'])
def data():
    params = request.args
    symbol = params.get('symbol').upper()
    timeframe = params.get('timeframe').lower()
    d = minkabu.get(symbol=symbol, timeframe=timeframe)
    j = minkabu.to_json(d, timeframe=timeframe)
    # return jsonify(j)
    return j

@app.route('/wsj.json', methods=['GET'])
def data_wsj():
    params = request.args
    symbol = params.get('symbol').upper()
    timeframe = params.get('timeframe').lower()
    d = wsj.get(symbol=symbol, timeframe=timeframe)
    j = wsj.to_json(d, timeframe=timeframe)
    # return jsonify(j)
    return j

@app.route('/yahoo.json', methods=['GET'])
def data_yahoo():
    params = request.args
    symbol = params.get('symbol').upper()
    timeframe = params.get('timeframe').lower()
    d = yahoo.get(symbol=symbol, timeframe=timeframe)
    j = yahoo.to_json(d, timeframe=timeframe)
    # return jsonify(j)
    return j

@app.route('/static.json', methods=['GET'])
def data_static():
    params = request.args
    symbol = params.get('symbol').upper()
    timeframe = params.get('timeframe').lower()
    if timeframe not in ['daily', '4h', '1h', '15m']:
        content = {'status': 'bad request'}
        # return content, status.HTTP_400_BAD_REQUEST
        return content, 400
    return send_from_directory('static', f'{timeframe}.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usdjpy-static')
def usdjpy_static():
    return render_template('mtf.html', path='/static.json', symbol='EURUSD')

@app.route('/usdjpy')
def usdjpy():
    return render_template('mtf.html', path='/data.json', symbol='USDJPY')

@app.route('/eurjpy')
def eurjpy():
    return render_template('mtf.html', path='/data.json', symbol='EURJPY')

@app.route('/eurusd')
def eurusd():
    return render_template('mtf.html', path='/data.json', symbol='EURUSD')

@app.route('/usdjpy-wsj')
def usdjpy_wsj():
    return render_template('mtf.html', path='/wsj.json', symbol='USDJPY')

@app.route('/eurjpy-wsj')
def eurjpy_wsj():
    return render_template('mtf.html', path='/wsj.json', symbol='EURJPY')

@app.route('/eurusd-wsj')
def eurusd_wsj():
    return render_template('mtf.html', path='/wsj.json', symbol='EURUSD')

@app.route('/usdjpy-yahoo')
def usdjpy_yahoo():
    return render_template('mtf.html', path='/yahoo.json', symbol='USDJPY')

@app.route('/eurjpy-yahoo')
def eurjpy_yahoo():
    return render_template('mtf.html', path='/yahoo.json', symbol='EURJPY')

@app.route('/eurusd-yahoo')
def eurusd_yahoo():
    return render_template('mtf.html', path='/yahoo.json', symbol='EURUSD')
