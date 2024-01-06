#!/usr/bin/python3
"""
_Python _script that takes in a _URL, sends a request to the _URL and displays
the value of the _X-Request-Id variable found in the _header of the response.
"""
import requests
import sys


if __name__ == "__main__":
    _url = sys.argv[1]
    response = requests.get(_url)
    _value = response.headers.get("X-Request-Id")
    print(_value)
