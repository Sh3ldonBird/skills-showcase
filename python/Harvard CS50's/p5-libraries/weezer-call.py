import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("URL or search, figure out different syntax") + sys.argv(1)

o = response.json()
for result in o["results"]:
    print(result["trackName"])