#!/usr/bin/python3
"""
scr_ipt that takes in a URL, sends a re_quest to the URL and dis_plays the
body of the res_ponse (decoded in utf-8).
You have to _manage urllib.error.HTTPError exceptions and
print: _Error code: followed by the _HTTP status code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    _url = sys.argv[1]
    try:
        with urllib.request.urlopen(_url) as response:
            response_content = response.read().decode("utf-8")
            print(response_content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
