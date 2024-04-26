#!/usr/bin/python3
"""script that takes in a URL, 
sends a request to the URL and 
displays the value of the X-Request-Id variable"""

if __name__ == '__main__':
    import urllib.request
    import sys

    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as result:
        print(dict(result.headers)['X-Request-Id'])

