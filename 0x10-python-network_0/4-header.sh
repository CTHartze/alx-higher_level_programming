#!/bin/bash
# Bash script takes in URL as an argument, sends GET request, and displays body of the response
curl -sH "X-School-User-Id: 98" "${1}"
