'''
The MIT License (MIT)

Copyright (c) 2016 Hirokazu Kiyomaru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
