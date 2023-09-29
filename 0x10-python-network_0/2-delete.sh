#!/bin/bash
# Script that ends a DELETE request to URL passed as the first argument
curl -sX "DELETE" "$1"
