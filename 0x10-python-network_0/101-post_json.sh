#!/bin/bash
# Sends the JSON POST request to the given URL with the given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
