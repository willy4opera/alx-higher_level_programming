#!/usr/bin/python3
"""The script:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authnc = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    re = requests.get("https://api.github.com/user", auth=authnc)
    print(re.json().get("id"))
