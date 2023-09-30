#!/usr/bin/python3
""" 
Script that takes a URL, sends a request to URL, and displays the body
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            response_encoding = response.headers.get_content_charset('utf-8')
            response_body = response.read().decode(response_encoding)
            print(response_body)
    except error.HTTPError as er:
        print('Error code:', er.code)
