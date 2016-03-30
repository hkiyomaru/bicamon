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

def send_to_viewer(fired_module):
    req = urllib2.Request('http://localhost:5000/api')
    req.add_header('Content-Type', 'application/json')
    send_data = {
        "cells":[fired_module]
    }
    res = urllib2.urlopen(req, json.dumps(send_data))

# test code
if __name__ == '__main__':
    for i in range(5000):
        send_to_viewer("CA1")
        send_to_viewer("CS")
        send_to_viewer("CA3")
        send_to_viewer("ENTl")
        send_to_viewer("AAA")
        send_to_viewer("AN")
        send_to_viewer("SM")
        send_to_viewer("PYR")
        send_to_viewer("PRM")
        send_to_viewer("MOB")
        send_to_viewer("AON")
        send_to_viewer("OT")
        send_to_viewer("VISC")
        send_to_viewer("CEA")
        send_to_viewer("ACB")
        send_to_viewer("MS")
        send_to_viewer("CM")
        send_to_viewer("RE")
        send_to_viewer("PR")
        send_to_viewer("TR")
        send_to_viewer("SSp-n")
        send_to_viewer("SSs")
        send_to_viewer("CP")
        send_to_viewer("AUDp")
        send_to_viewer("AUDv")
        send_to_viewer("SCs")
        send_to_viewer("RSPv")
        send_to_viewer("RSPd")
        send_to_viewer("PAG")
        send_to_viewer("NLL")
    
