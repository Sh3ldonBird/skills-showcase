# OWASP TOP 10 API
The Open Web Application Security Project (OWASP) released the updated API Security Top 10 list in 2023. I will be using this list to showcase vulnerabilities within several applications.

---

**API1:2023 – Broken Object Level Authorization (BOLA)**

**Description:** APIs often expose endpoints that handle object identifiers, creating a broad attack surface for object-level access control issues. Without proper authorization checks, attackers can manipulate object IDs to access data they are not authorized to view or modify.

**Impact:** Exploitation can lead to unauthorized access to sensitive data, data leakage, and potential data manipulation.

**Testing Methodology:**
- Identify endpoints that handle object identifiers.
- Attempt to access or modify objects owned by other users by tampering with object IDs.
- Verify if proper authorization checks are in place to prevent unauthorized access.

---

**API2:2023 – Broken Authentication**

**Description:** Improper implementation of authentication mechanisms can allow attackers to compromise authentication tokens or exploit flaws to assume other users' identities.

**Impact:** Leads to unauthorized access, data breaches, and potential full system compromise.

**Testing Methodology:**
- Assess the strength and implementation of authentication mechanisms.
- Test for vulnerabilities like credential stuffing, brute force attacks, and token mismanagement.
- Ensure multi-factor authentication (MFA) is implemented where appropriate.

---

**API3:2023 – Broken Object Property Level Authorization**

**Description:** This vulnerability arises from the lack of or improper authorization validation at the object property level, leading to information exposure or manipulation by unauthorized parties.

**Impact:** Unauthorized users can access or modify sensitive object properties, leading to data breaches.

**Testing Methodology:**
- Review API responses to identify exposed object properties.
- Attempt to modify object properties without proper authorization.
- Ensure that property-level authorization checks are enforced.

---

**API4:2023 – Unrestricted Resource Consumption**

**Description:** APIs require resources like network bandwidth, CPU, memory, and storage. Lack of restrictions can lead to resource exhaustion, causing Denial of Service (DoS) attacks or increased operational costs.

**Impact:** Service disruption, degraded performance, and financial losses due to overconsumption of resources.

**Testing Methodology:**
- Perform load testing to evaluate resource handling.
- Check for rate limiting and throttling mechanisms.
- Ensure APIs have safeguards against resource exhaustion attacks.

---

**API5:2023 – Broken Function Level Authorization**

**Description:** Complex access control policies with different hierarchies, groups, and roles can lead to authorization flaws, especially when there's an unclear separation between administrative and regular functions.

**Impact:** Attackers can access or execute functions beyond their privileges, leading to unauthorized actions.

**Testing Methodology:**
- Map out API endpoints and their required authorization levels.
- Attempt to access administrative functions with non-administrative accounts.
- Verify that role-based access controls are correctly implemented.

---

**API6:2023 – Unrestricted Access to Sensitive Business Flows**

**Description:** APIs may expose business-critical operations without adequate access controls, allowing attackers to execute sensitive transactions.

**Impact:** Unauthorized transactions can lead to financial fraud, data manipulation, and reputational damage.

**Testing Methodology:**
- Identify sensitive business operations exposed via APIs.
- Attempt to perform these operations without proper authorization.
- Ensure that sensitive operations have strict access controls.

---

**API7:2023 – Server-Side Request Forgery (SSRF)**

**Description:** SSRF vulnerabilities occur when an API fetches a remote resource without validating the user-supplied URL, allowing attackers to make requests to unintended destinations.

**Impact:** Can lead to unauthorized access to internal systems, data exfiltration, and potential system compromise.

**Testing Methodology:**
- Identify API endpoints that accept URLs or fetch remote resources.
- Attempt to supply malicious URLs to initiate unauthorized requests.
- Ensure proper validation and sanitization of user-supplied URLs.

---

**API8:2023 – Security Misconfiguration**

**Description:** Improper configurations, such as default settings, incomplete configurations, or exposed debug endpoints, can lead to vulnerabilities.

**Impact:** Attackers can exploit misconfigurations to gain unauthorized access or information about the system.

**Testing Methodology:**
- Review API configurations for default credentials, unnecessary services, and exposed endpoints.
- Ensure that security settings are hardened and properly configured.
- Conduct regular configuration audits.

---

**API9:2023 – Improper Inventory Management**

**Description:** Lack of proper documentation and management of APIs can lead to forgotten or unmanaged endpoints, increasing the attack surface.

**Impact:** Unmanaged APIs can be exploited, leading to data breaches and unauthorized access.

**Testing Methodology:**
- Conduct an inventory of all API endpoints.
- Identify and assess deprecated or undocumented APIs.
- Ensure that all APIs are documented and monitored.

---

**API10:2023 – Unsafe Consumption of APIs**

**Description:** Trusting data from third-party APIs without proper validation can introduce vulnerabilities, especially if those APIs are compromised.

**Impact:** Can lead to data corruption, security breaches, and integration of malicious content.

**Testing Methodology:**
- Assess the trustworthiness and security practices of third-party APIs.
- Implement input validation and sanitization for data received from 