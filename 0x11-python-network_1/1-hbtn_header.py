#!/usr/bin/python3
""" This checks a header parameter"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        X_Request_Id = response.getheader('X-Request-Id')
        print(X_Request_Id)
