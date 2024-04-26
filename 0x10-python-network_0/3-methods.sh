#!/bin/bash
#this script outputs all HTTP methods the server of a specific URL will accept.
curl -sI "$1" | grep "Allow" | cut -f2 -d: | sed 's/^[[:space:]]//'

