import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load JSON file within the same directory to for parsing, flattening, and then visualization.
with open("/home/sheldon/github/skills-showcase/python/log-parsing/JSON-files/?/AWS-security-hub.json", "r") as JSON_file:
    json_data = JSON_file.read()
if not json_data.strip():
    print("Error: The file is empty or not formatted properly")
else:
    try:
        log_data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
#for item in log_data:
#    if isinstance(item.get("Severity"), dict):
#        severity_label = item ["Severity"].get("Label", "Unknown")
#        title = item.get("Title", "No Title")
#        resource_type = item.get("Resources",[{}][0].get("Type", "Unknown"))
#        flattened_data = []
#        flattened_data.append({
#            "Severity": severity_label,
#            "Title": title,
#            "ResourceTyp": resource_type
#        })
#    else:
#        print(f"Error: 'Severity' is not a dictionary in item {item["Id"]}")

##for item in log_data:
##    isinstance(item.get("Severity"), dict)
##    severity_label = item ["Severity"].get("Label", "Unknown")
##    title = item.get("Title", "No Title")
##    resource_type = item.get("Resources",[{}][0].get("Type", "Unknown"))
##    flattened_data = []
##    flattened_data.append({
##        "Severity": severity_label,
##        "Title": title,
##        "ResourceTyp": resource_type
##    })

flattened_data = []

for item in log_data:
    isinstance(item.get("Severity"), dict)
    severity_label = item.get("Severity",{}).get("Label", "Unknown")
    title = item.get("Title", "No Title")
    resource_type = None
    if item.get("Resources"):
        resource_type = item["Resources"][0].get("Type", "Unknown") if item ["Resources"] else None

    flattened_data.append({
        "Severity": severity_label,
        "Title": title,
        "ResourceType": resource_type
    })

# Flatten the data to extract only Severity Label, Title, and Resource Type
#flattened_data = []
#for item in loop_data:
#    severity_label = item["Severity"]["Label"]
#    title = item["Title"]
#    resource_type = item['Resources'][0]['Type'] if item['Resources'] else None
#    flattened_data.append({
#        'Severity': severity_label,
#        'Title': title,
#        'ResourceType': resource_type
#    })

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(flattened_data)

# Display the DataFrame (optional)
#print(df)

# Visualization: Count of findings by Severity
plt.figure(figsize=(8, 5))
sns.countplot(x='Severity', data=df, palette='Set2')
plt.title('Count of Findings by Severity')
plt.xlabel('Severity')
plt.ylabel('Count')
plt.show()

# Visualization: Count of Findings by Resource Type
plt.figure(figsize=(8, 5))
sns.countplot(x='ResourceType', data=df, palette='Set3')
plt.title('Count of Findings by Resource Type')
plt.xlabel('Resource Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
