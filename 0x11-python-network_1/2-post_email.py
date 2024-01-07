#!/usr/bin/python3
"""this mehod makes post request using urlib"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    encoded = urllib.parse.urlencode(data).encode('ascii')
    with urllib.request.urlopen(encoded, data=encoded) as response:
        print(response.read().decode('utf-8'))
