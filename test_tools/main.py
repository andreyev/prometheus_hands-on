#!/usr/bin/env python3
# Code originally posted on: https://stackoverflow.com/questions/70787302/does-prometheus-supports-webhooks/70791409

import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={"err": ""})
@app.errorhandler(404)
@app.errorhandler(405)
def print_request(err):
    if request.json:
        body = json.dumps(request.json, indent=4, sort_keys=True)
    elif request.form:
        body = request.form
    else:
        body = request.data

    print(f"{request.method} {request.path}\n"
          "#################### HEADERS ###################\n"
          f"{request.headers}"
          "--------------------- BODY ---------------------\n"
          f"{body}")
    return "OK\n"
if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)