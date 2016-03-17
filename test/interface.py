import json
import urllib2
import time

def send_request(module):
    req = urllib2.Request('http://localhost:5000/api')
    req.add_header('Content-Type', 'application/json')
    send_data = {
        "cells":[module]
    }
    res = urllib2.urlopen(req, json.dumps(send_data))

# test code
if __name__ == '__main__':
    fired_module = "CA1"
    send_request(fired_module)
