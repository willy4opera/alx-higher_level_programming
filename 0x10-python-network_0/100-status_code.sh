#!/bin/bash
# Sends the GET request to the given URL and display response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
