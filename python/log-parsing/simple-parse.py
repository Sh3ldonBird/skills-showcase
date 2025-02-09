# Allows arguements to be presented while calling the .py file
# Modify to pull in log requests and then parse out data quickly
# Modify to then send to a dictionary, database, list, etc.

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("URL or search, figure out different syntax") + sys.argv(1)

o = response.json()
for result in o["results"]:
    print(result["trackName"])