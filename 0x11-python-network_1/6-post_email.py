#!/usr/bin/python3
"""Takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter"""

import sys
import requests

if __name__ == '__main__':

    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    reque_ = requests.post(url, data=val)
    print(reque_.text)
