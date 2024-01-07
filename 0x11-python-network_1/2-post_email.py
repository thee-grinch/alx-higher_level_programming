#!/usr/bin/python3
"""this mehod makes post request using urlib"""

import urllib.request
import urllib.parse

if __name__ == "__main__":
    encoded = urllib.parse.urlencode({'email': $2}).encode('utf-8')
    with urllib.request.urlopen($1, data=encoded) as response:
        print(response.read().decode('utf-8'))
