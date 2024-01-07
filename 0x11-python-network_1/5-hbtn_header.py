#!/usr/bin/python3
"""this checks the response header"""
import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
