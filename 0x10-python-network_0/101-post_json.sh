#!/bin/bash
# Sends post request with json data passed as first argument
curl -X POST -s -H "Content-Type: application/json" -d @"$2" "$1"

