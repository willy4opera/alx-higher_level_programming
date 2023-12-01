#!/usr/bin/python3
"""This script:
takes in URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    Resour = sys.argv[1]

    result = urllib.request.Request(Resour)
    with urllib.request.urlopen(result) as response:
        print(dict(response.headers).get("X-Request-Id"))
