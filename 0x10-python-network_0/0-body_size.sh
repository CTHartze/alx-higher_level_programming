#!/bin/bash
# Bash script takes in URL, sends request and displays size of the body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
