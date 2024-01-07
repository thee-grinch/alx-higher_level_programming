#!/usr/bin/python3
"""this checks the reponse header"""
import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    with requests.get(' https://api.github.com/user', auth=(sys.argv[1], sys.argv[2])) as response:
        print(response.json().get('id'))
