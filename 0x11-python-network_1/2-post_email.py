#!/usr/bin/python3
"""
_script that takes in a _URL and an email, sends a POST _request to the passed
URL with the _email as a _arameter, and displays the _body of the _response
_(decoded in _utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    _param = {
        "email": email
    }
    _query_string = urllib.parse.urlencode(_param)
    _data = _query_string.encode("utf-8")
    _req = urllib.request.Request(url, _data=_data)
    with urllib.request.urlopen(_req) as response:
        response_content = response.read().decode("utf-8")
        print(response_content)
