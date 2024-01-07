#!/usr/bin/python3
"""this checks the response header"""
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    with requests.post('http://0.0.0.0:5000/search_user', json=data) as response:
        try:
            data = response.json()
        except Exception:
            print("Not a valid JSON")
        try:
            print("[{}] {}".format(data['id'], data['name']))
        except Exception:
            print("No Result")
