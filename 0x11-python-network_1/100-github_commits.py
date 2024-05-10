#!/usr/bin/python3

import requests
import sys

repository = sys.argv[1]
owner = sys.argv[2]
url = f'https://api.github.com/repos/{owner}/{repository}'

response = requests.get(url)
data = response.json()

print(data['id'])

