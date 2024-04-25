#!/bin/bash
#this script outputs all HTTP methods the server of a specific URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

