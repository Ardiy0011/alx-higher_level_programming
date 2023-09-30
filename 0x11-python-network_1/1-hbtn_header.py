#!/usr/bin/python3
"""
Function that sends an HTTP request and retrieves the X-Request-Id variable
"""
import urllib.request
import sys

url = sys.argv[1]


def get_x_request_id(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)


get_x_request_id(url)
