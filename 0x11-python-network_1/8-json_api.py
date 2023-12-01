#!/usr/bin/python3
"""The script:
takes in a letter
sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    le = "" if len(sys.argv) == 1 else sys.argv[1]
    pld = {"q": le}

    re = requests.post("http://0.0.0.0:5000/search_user", data=pld)
    try:
        response = re.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
