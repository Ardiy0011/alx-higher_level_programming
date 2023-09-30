#!/usr/bin/python3
"""module that fetches url"""
if __name__ == '__main__':
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        """fetching with request"""
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- body: {}".format(body))
        print("\t- utf8 body: {}".format(body.decode('utf-8')))
