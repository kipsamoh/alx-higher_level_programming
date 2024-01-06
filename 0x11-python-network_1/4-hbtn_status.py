#!/usr/bin/python3
"""
_script that _fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    _url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(_url)
    content = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
