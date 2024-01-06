#!/usr/bin/python3
"""
_script that takes in a letter and s_ends a POST request to
_http://0.0.0.0:5000/search_user with the letter as a _parameter.
The letter must be sent in the _variable q.
If no argument is given, _set q="".
If the response body is properly JSON formatted and not empty, display the
id and name like this: [<id>] <name>, _Otherwise: Display Not a valid _JSON
if the JSON is _invalid and Display No _result if the JSON i_s empty
"""
import sys
import requests


if __name__ == "__main__":
    _url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    pay_load = {"q": q}
    response = requests.post(_url, data=pay_load)
    try:
        _json_outp = response.json()
        if not _json_outp:
            print("No result")
        else:
            my_id = _json_outp.get("id")
            my_name = _json_outp.get("name")
            print("[{}] {}".format(my_id, my_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
