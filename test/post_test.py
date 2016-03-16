import json
import urllib2
import time

data1 = { 
    "cells":["CA3", "DG", "ENTl"]
}

data2 = { 
    "cells":["CA1", "ENTm", "PRE", "PIR"]
}

data3 = {
    "cells":["POST", "PAR"]
}

req1 = urllib2.Request('http://localhost:5000/api')
req1.add_header('Content-Type', 'application/json')

req2 = urllib2.Request('http://localhost:5000/api')
req2.add_header('Content-Type', 'application/json')

req3 = urllib2.Request('http://localhost:5000/api')
req3.add_header('Content-Type', 'application/json')


for i in range(5000):
    response = urllib2.urlopen(req1, json.dumps(data1))
    # time.sleep(0.4)
    response = urllib2.urlopen(req2, json.dumps(data2))
    # time.sleep(0.4)
    response = urllib2.urlopen(req3, json.dumps(data3))
    # time.sleep(0.6)
