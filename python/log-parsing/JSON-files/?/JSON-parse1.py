import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# JSON file within the same directory to be loaded for parsing, flattening, and then visualization.
json_data = "AWS-security-hub.json"


# Parse the JSON data
data = json.loads(json_data)

# Flatten the data to extract only Severity Label, Title, and Resource Type
flattened_data = []
for item in data:
    severity_label = item['Severity']['Label']
    title = item['Title']
    resource_type = item['Resources'][0]['Type'] if item['Resources'] else None
    flattened_data.append({
        'Severity': severity_label,
        'Title': title,
        'ResourceType': resource_type
    })

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(flattened_data)

# Display the DataFrame (optional)
print(df)

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
