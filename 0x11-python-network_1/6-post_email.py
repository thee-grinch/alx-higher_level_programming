#!/usr/bin/python3
"""this checks the response header"""
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    url = sys.argv[1]
    with requests.post(url, data=data) as response:
        print(response.text)
