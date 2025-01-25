#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import os

import MetaTrader5 as mt5


def init(path) -> None:
    path = get_backup_mt5path() if path is None or path == '' else path
    if not mt5.initialize(path):
        print("initialize() failed, error code =", mt5.last_error())
        quit()


def get_backup_mt5path() -> str:
    backup_paths = [
        'C:/Program Files/MT5 by FOREX.com Global CN/terminal64.exe',
        'C:/Program Files/mt5/terminal64.exe',
        '/headless/.wine/drive_c/Program\ Files/mt5/terminal64.exe',
    ]
    paths = list(filter(lambda path_: os.path.exists(path_), backup_paths))
    return paths[0] if paths is not None and len(paths) > 0 else None


def time_frame_mapping(time_frame):
    if 'M1' == time_frame:
        return mt5.TIMEFRAME_M1
    if 'M5' == time_frame:
        return mt5.TIMEFRAME_M5
    if 'M15' == time_frame:
        return mt5.TIMEFRAME_M15
    if 'M30' == time_frame:
        return mt5.TIMEFRAME_M30
    if 'H1' == time_frame:
        return mt5.TIMEFRAME_H1
    if 'H4' == time_frame:
        return mt5.TIMEFRAME_H4
    if 'D1' == time_frame:
        return mt5.TIMEFRAME_D1
    if 'W1' == time_frame:
        return mt5.TIMEFRAME_W1
    if 'MN1' == time_frame:
        return mt5.TIMEFRAME_MN1
    return None


def copy_rates_from(symbol, time_frame, date_from, count) -> list:
    return mt5.copy_rates_from(symbol, time_frame_mapping(time_frame), date_from, int(count))


def symbol_info(symbol):
    return mt5.symbol_info(symbol)


def get_symbols():
    return mt5.symbols_get()
