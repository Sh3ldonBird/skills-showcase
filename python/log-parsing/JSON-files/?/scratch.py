import json

# Load the JSON data from a file
with open('log_file.json', 'r') as file:
    json_data = json.load(file)


import pandas as pd

# Load JSON data directly into a DataFrame
df = pd.read_json('log_file.json')
