#!/bin/bash
#Accepts URL input, sends a POST request to passed URL,and displays the response.
curl -X POST -s -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
