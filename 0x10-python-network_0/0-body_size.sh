#!/bin/bash
# takes in a URL.
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
