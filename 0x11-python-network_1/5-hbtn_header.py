#!/usr/bin/python3
"""
Script takes in URL, sends request, and displays
the header variable from the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
