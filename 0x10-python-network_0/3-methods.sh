#!/bin/bash
# Bash script takes in URL and display all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
