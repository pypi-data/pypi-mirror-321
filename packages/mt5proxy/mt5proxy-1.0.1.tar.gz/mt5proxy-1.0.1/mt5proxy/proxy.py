#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import datetime

import pandas as pd
import pytz
from flask import Flask
from flask.globals import request

from . import mt5client

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return "Leave me alone."


@app.route("/copy_rates_from", methods=["get", "post"])
def copy_rates_from():
    symbol = request.args.to_dict().get("symbol")
    time_frame = request.args.to_dict().get("time_frame")
    date_from = request.args.to_dict().get("date_from")
    count = request.args.to_dict().get("count")
    date_from = datetime.datetime.strptime(date_from, "%Y%m%d%H%M%S").astimezone(pytz.timezone("Etc/UTC"))
    rates = mt5client.copy_rates_from(symbol, time_frame, date_from, count)
    rates_frame = pd.DataFrame(rates)
    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
    ohlcs = []
    for row in rates_frame.iterrows():
        ohlc = {}
        ohlc['symbol'] = symbol
        ohlc['time_frame'] = time_frame
        ohlc['bar_time'] = row[1]['time'].strftime("%Y-%m-%d %H:%M:%S")
        ohlc['open'] = row[1]['open']
        ohlc['high'] = row[1]['high']
        ohlc['low'] = row[1]['low']
        ohlc['close'] = row[1]['close']
        ohlcs.append(ohlc)
    return ohlcs


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8082)
