#!/usr/bin/python3
"""
Script takes in URL, sends a request, handles the response
status code, and retrieves the response body.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
