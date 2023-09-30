#!/bin/bash
# Script that ends a DELETE request to URL passed as the first argument
response=$(curl -sX "DELETE" "$1")
echo "$response"