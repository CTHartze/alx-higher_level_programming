#!/usr/bin/python3
"""
Script takes in URL and an email address, sends POST request to
passed URL with email, and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
