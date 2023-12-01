#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url_re = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(url_re.text)))
    print("\t- content: {}".format(url_re.text))
