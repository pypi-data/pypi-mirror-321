#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
import os
import sys

from . import mt5client
from . import proxy

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))


def main():
    mt5path = sys.argv[1] if len(sys.argv) > 1 else None
    port = sys.argv[2] if len(sys.argv) > 2 else 8082
    mt5client.init(mt5path)
    proxy.app.run(debug=False, host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
