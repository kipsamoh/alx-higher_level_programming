#!/usr/bin/python3
"""
_script that takes in a _URL and an _email, sends a _POST request to the passed
_URL with the _email as a _parameter, and _displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    _url = sys.argv[1]
    email = sys.argv[2]
    pay_load = {
        "email": email
    }
    response = requests.post(_url, data=pay_load)
    print(response.text)
