#!/usr/bin/python3
"""
_script that _fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    _url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(_url)
    _contents = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(_contents)))
    print('\t- _contents: {}'.format(_contents))
