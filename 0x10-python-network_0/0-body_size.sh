#!/bin/bash
# Obtainss byte size of the HTTP response header for specific URL.
curl -s "$1" | wc -c

