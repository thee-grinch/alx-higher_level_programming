#!/usr/bin/python3
"""this checks the response header"""
import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
