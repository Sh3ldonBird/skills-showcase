# Objective:
Develop a Python application to retrieve and analyze recent vulnerability data from the National Vulnerability Database (NVD) API.
# Exercises: 
- API Integration  
  - Connect to the NVD API (Documentation: https://nvd.nist.gov/developers/vulnerabilities)  
  - Retrieve CVE data for the last 5 days  
- Data Parsing  
  - Extract relevant information from the API response in order to:  
  - Calculate total number of CVEs published in last 5 days  
  - Determine average CVSS v3.1  base score  
  - Identify CVE/s with highest CVSS v3.1 base score  
  - Amount of CVEs by base CVSS v3.1 severity levels  
- Results Presentation  
  - Display analysis results in a clear, readable format  
  - (Bonus) Create a visual representation of CVSS score distribution  


# Example Output  
Fetching CVEs from 2024-09-18 to 2024-10-18...  

Total CVEs: 2785  
Average CVSS Score: 6.93  

Highest CVSS Score:  
  CVE ID: CVE-2024-42017  
  CVSS Score: 10.0  
  Description: An issue was discovered in Atos Eviden iCare 2.7.1 through 2.7.11. The application exposes a web int...  

CVEs by Severity:  
  HIGH: 1041  
  MEDIUM: 1154  
  CRITICAL: 293  
  LOW: 69  
  NONE: 11  
