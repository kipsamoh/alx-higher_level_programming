#!/usr/bin/python3
"""_script that takes your _GitHub credentials (username and password) and
uses the _GitHub API to display your id.
The first _argument will be your _username.
The _second argument will be your _password (in your case, a personal
access token as _password).
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    _url = "https://api.github.com/user"
    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    response = requests.get(_url, auth=HTTPBasicAuth(user_name, pass_word))
    json_objt = response.json()
    print(json_objt.get("id"))
