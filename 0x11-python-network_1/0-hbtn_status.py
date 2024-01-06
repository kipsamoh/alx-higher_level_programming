#!/usr/bin/python3
"_Module that _fetches https://alx-intranet.hbtn.io/status"
import urllib.request


if __name__ == "__main__":
    _url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(_url) as response:
        _html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(_html)))
        print('\t- content: {}'.format(_html))
        print('\t- utf8 content: {}'.format(_html.decode("utf-8")))
