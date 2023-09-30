#!/usr/bin/python3
"""module that fetches url"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    """fetching with request"""
    body = response.read()
    print("Body response:")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", body.decode('utf-8'))
