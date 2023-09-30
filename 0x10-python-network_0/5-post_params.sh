#!/bin/bash
# Script sends POST http method to URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
