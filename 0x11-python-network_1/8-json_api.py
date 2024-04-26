#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    reque_ = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_dict = reque_.json()
        id = req_dict.get('id')
        name = req_dict.get('name')
        if len(req_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
    except:
        print("Not a valid JSON")
