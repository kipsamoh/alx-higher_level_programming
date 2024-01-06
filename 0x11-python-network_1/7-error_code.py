#!/usr/bin/python3
"""
_script that takes in a _URL, sends a _request to the URL and _displays the
body of the _response (decoded in utf-8).
If the HTTP status code is greater than or equal to 400, print:
Error code: _followed by the value of the _HTTP status code.
"""
import sys
import requests


if __name__ == "__main__":
    _url = sys.argv[1]
    response = requests.get(_url)
    _body = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(_body)
