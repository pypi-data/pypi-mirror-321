#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import os

import MetaTrader5 as mt5
from knify import listutil
from knify import objutil


def get_backup_mt5path() -> str:
    backup_paths = [
        'C:/Program Files/MT5 by FOREX.com Global CN/terminal64.exe',
        'C:/Program Files/mt5/terminal64.exe',
        '/headless/.wine/drive_c/Program\ Files/mt5/terminal64.exe',
    ]
    paths = list(filter(lambda path_: os.path.exists(path_), backup_paths))
    return listutil.find_first(paths)


def init(path):
    path = objutil.default_if_none(path, get_backup_mt5path())
    if not mt5.initialize(path):
        print("initialize() failed, error code =", mt5.last_error())
        quit()
