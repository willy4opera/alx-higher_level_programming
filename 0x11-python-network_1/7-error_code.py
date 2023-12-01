#!/usr/bin/python3
"""The script that
takes in a URL
sends a request to the URL
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url_re = sys.argv[1]

    req = requests.get(url_re)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
