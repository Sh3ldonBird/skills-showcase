import requests
import json


#r = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0/?lastModStartDate=2025-02-05T13:00:00.000%2B01:00&lastModEndDate=2025-02-10T13:36:00.000%2B01:00')
#data = r.json()
#
# print(r.status_code)
#
#
#with open("filename.json", "w") as JSON_log:
#    json.dump(data, JSON_log, indent=4)

with open("/home/sheldon/github/bugcrowd-interview/filename.json", 'r') as json_data:

    data = json.load(json_data)
vuln_base = data.get("vulnerabilities")
for item in json_data:
   

    print(vuln_base)

    """
    Calculate total number of CVEs published in last 5 days
    Determine average CVSS v3.1  base score
    dentify CVE/s with highest CVSS v3.1 base score
    mount of CVEs by base CVSS v3.1 severity levels

    """




    """
    Results Presentation
        Display analysis results in a clear, readable format
        (Bonus) Create a visual representation of CVSS score distribution

    """