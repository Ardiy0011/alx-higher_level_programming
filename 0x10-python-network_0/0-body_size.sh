#!/bin/bash
# takes in a URL and sends a request that displays the size of the body of the response
url="$1"
response_file=$(mktemp)
curl -sI "$url" -o "$response_file"
size=$(wc -c < "$response_file")

echo "$size"
