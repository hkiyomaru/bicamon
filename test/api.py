"""A function to send request to BiCAmon."""
import json
import urllib2


def send_to_viewer(fired_module):
    """Send a POST request to BiCAmon server."""
    req = urllib2.Request('http://localhost:5000/api')
    req.add_header('Content-Type', 'application/json')

    send_data = {
        "cells": [fired_module]
    }

    res = urllib2.urlopen(req, json.dumps(send_data))

    return res


# test code
if __name__ == '__main__':
    module_name = "CA1"
    send_to_viewer(module_name)
