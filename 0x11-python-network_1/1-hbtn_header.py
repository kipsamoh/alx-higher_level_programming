#!/usr/bin/python3
"""
_Python script that _takes in a URL, sends a _request to the URL and displays
the value of the _X-Request-Id variable found in the _header of the _response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        _value = html.get('X-Request-Id')
        print(_value)
