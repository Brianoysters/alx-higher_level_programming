#!/bin/bash
# Sends post request with json data passed as first argument
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
