#!/bin/bash
# script that takes in a URL, sends GET request and displays body of response
url="$1"

# Send a GET request and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Check the HTTP status code of the response
http_status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
