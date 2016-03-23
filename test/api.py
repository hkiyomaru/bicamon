import json
import urllib2

def send_to_viewer(fired_module):
    req = urllib2.Request('http://localhost:5000/api')
    req.add_header('Content-Type', 'application/json')
    send_data = {
        "cells":[fired_module]
    }
    res = urllib2.urlopen(req, json.dumps(send_data))

# test code
if __name__ == '__main__':
    fired_module = "CA1"
    send_to_viewer(fired_module)