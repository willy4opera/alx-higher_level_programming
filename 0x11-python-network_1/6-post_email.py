#!/usr/bin/python3

"""The script:
takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable
found in the header ofthe response.
"""

from sys import argv
import requests


if __name__ == '__main__':
    response = requests.post(argv[1], {'email': argv[2]})
    print(response.text)
