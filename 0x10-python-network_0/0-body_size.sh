#!/bin/bash
# Obtainss byte size of the HTTP response header for specific URL.
curl -sI "$1" | grep "Content-Length" | cut -f2 -d" "
