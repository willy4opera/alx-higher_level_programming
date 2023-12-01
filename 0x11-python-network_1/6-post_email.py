#!/usr/bin/python3

"""The script:
takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url_re = sys.argv[1]

    req = urllib.request.Request(url_re)
    with urllib.request.urlopen(req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
