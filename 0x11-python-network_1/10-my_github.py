#!/usr/bin/python3
"""Utilizes GitHub API to display a GitHub ID based on specified credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    authenticate = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    reque_ = requests.get("https://api.github.com/user", auth=authenticate)
    print(reque_.json().get("id"))
