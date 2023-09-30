#!/usr/bin/python3
"""
Function that sends an HTTP POST request with an email parameter
and retrieves the response body (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
mail = sys.argv[2]

def post_email(url, mail):
    data = {'email': mail}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)

post_email(url, mail)
