#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from flask import Flask
from flask.globals import request

app = Flask(__name__)


@app.route("/test", methods=["get"])
def order_graph():
    orderId = request.args.to_dict().get("id")
    return orderId + "_ hello"


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8082)
