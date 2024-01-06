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
    _data = _query_string.encode("ascii")
    _req = urllib.request.Request(url, _data)
    with urllib.request.urlopen(_req) as response:
        # _If you do not __pass the data __argument, urllib uses a GET _request.
        # __One way in which GET and POST _requests _differ is that POST _requests
        # __often have __"side-effects".
        response_content = response.read().decode("utf-8")
        print(response_content)
