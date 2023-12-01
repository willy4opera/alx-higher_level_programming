#!/usr/bin/python3
"""This script:
takes in a URL
sends a POST request to the passed URL
takes email as a parameter
displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url_res = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    resource = urllib.request.Request(url_res, data)
    with urllib.request.urlopen(resource) as response:
        print(response.read().decode("utf-8"))
