#!/usr/bin/env python
from flask import Flask, request
import json
import os
import subprocess

directory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.debug = True

GITHUB_IPS = [
  '207.97.227.253',
  '50.57.128.197',
  '108.171.174.178',
  '98.27.143.13',
  '127.0.0.1',
]

@app.route('/', methods=['GET', 'POST'])
def process_hook():
    if request.remote_addr not in GITHUB_IPS:
        return 'denied', 401
    if request.method == 'GET':
        return 'tee hee'
    payload = json.loads(request.form.get('payload'))
    url = payload['repository']['url'].replace('http://', 'https://')
    repo = url.split('/', 3)[-1]
    buildscript = directory + '/repos/' + repo + '/build.sh'
    if os.path.exists(buildscript):
        print 'Building ' + repo
        subprocess.call(['bash', buildscript])
        return ''
    else:
        return 'denied', 401

if __name__ == '__main__':
    app.run('0.0.0.0')
