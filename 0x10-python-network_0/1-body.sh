#!/bin/bash
# Bash script takes in URL, sends GET request, and displays body of 200 status code response
curl -Ls "$1"
