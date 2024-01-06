#!/usr/bin/python3
"""
_script that takes 2 arguments in order to list 10 commits (from the most
_ecent to oldest) of the _repository "rails" by the user "rails".
Print all _commits by: `<sha>: <author name>` (one by line)
The first argument will be the _repository name
The second _argument will be the _owner name
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repos_name = sys.argv[1]
        user_name = sys.argv[2]
        commmit_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(user_name, repos_name)
        response = requests.get(commmit_url)
        json_objt = response.json()
        for i, objt in enumerate(json_objt):
            if i == 10:
                break
            if type(objt) is dict:
                _name = objt.get('commit').get('author').get('name')
                print("{}: {}".format(objt.get('sha'), _name))
    except ValueError as invalid_json:
        pass
