#!/usr/bin/env python3
from urllib import response
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={"err": ""})
@app.errorhandler(404)
@app.errorhandler(405)
def print_request(err):
    return "OK\n"
@app.route("/sd")
def print_sd():
    data=app.response_class('[{"targets":["prometheus.io"],"labels":{"__meta_datacenter":"london","__meta_prometheus_job":"node"}}]',mimetype='application/json')
    return(data)
if __name__ == '__main__':
    app.run("0.0.0.0", port=8003)