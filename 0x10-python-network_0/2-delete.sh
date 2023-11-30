#!/bin/bash
# Bash script sends DELETE request to URL passed as the first argument and displays body of the response
curl -s "$1" -X DELETE
