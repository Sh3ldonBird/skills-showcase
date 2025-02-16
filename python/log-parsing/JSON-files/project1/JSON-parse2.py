import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("/home/sheldon/github/skills-showcase/python/log-parsing/JSON-files/?/AWS-guard-dog.json", "r") as JSON_file:
    JSON_data = JSON_file.read()
if not JSON_data.strip():
    print("Error: The file is empty")
else:
    try:
        log_data = json.loads(JSON_data)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
    #log_data = json.loads(JSON_data)

flattened_data = []

for item in log_data:
    #isinstance(item.get("Severity"), dict)
    severity_label = item.get("Severity").get("Label", None)
    severity_normalized = item.get("Severity").get("Normalized")
    title = item.get("Title", None)
    #resources_type = None
    if item.get("Resources"):
        resources_type = item.get("Resources")[0].get("Type", None) if item ["Resources"] else None



    flattened_data.append({
        "Severity": severity_label,
        "Normalized": severity_normalized,
        "Title": title,
        "Resource Type": resources_type
    })

#for entry in flattened_data:
#    print(entry)

df = pd.DataFrame(flattened_data)
#print(df)

plt.figure(figsize=(8,5))
sns.countplot(x='Severity')