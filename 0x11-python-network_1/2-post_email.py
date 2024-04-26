#!/usr/bin/python3
"""
 script that takes in a URL and an email, sends a POST request to the passed URL
"""


from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {}
    values['email'] = email

    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")

    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode("utf-8")
        print(page)
