#!/usr/bin/python3

"""Here, we display the X-Request-Id header variable of a request to a given URL
"""

import sys
import requests


if __name__ == "__main__":
    url_re = sys.argv[1]

    req = requests.get(url_re)
    print(req.headers.get("X-Request-Id"))
