#!/bin/bash
#Accepts URL as an argument, sends a GET request to the URL,and displays response body.
curl -sH "X-School-User-Id: 98" "$1"

