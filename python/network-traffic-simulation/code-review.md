# Overview
This document reviews [network-traffic.py](skills-showcase/python/network-traffic-simulation/network-traffic.py) at each code snippet to review the output given after running the docker container built and ran for this demonstration.

## Container Output
This is the following output that is generated when the python code below is ran when the container is started.
```Container-Output
IP: 192.168.1.3, Action: allow, Random: 9503
IP: 192.168.1.12, Action: allow, Random: 2391
IP: 192.168.1.8, Action: allow, Random: 4941
IP: 192.168.1.18, Action: allow, Random: 2367
IP: 192.168.1.12, Action: allow, Random: 8592
IP: 192.168.1.4, Action: block, Random: 8616
IP: 192.168.1.12, Action: allow, Random: 7708
IP: 192.168.1.9, Action: block, Random: 6352
IP: 192.168.1.18, Action: allow, Random: 2456
IP: 192.168.1.2, Action: allow, Random: 2404
IP: 192.168.1.16, Action: block, Random: 5907
IP: 192.168.1.5, Action: allow, Random: 4527
```
## Why

Straight forward library import of the internal 'random' python library.
```Python
import random  # Import the random module to generate random numbers
```
Start of defining variables  

User defined function that uses a formatted string in conjunction with a the random libraries function "randint" to create an integer between 0 & 20.
``` Python
def generate_random_ip():
    """Generate a random IP address."""
    # Create an IP address in the "192.168.1.x" range with a random last octet between 0 and 20
    return f"192.168.1.{random.randint(0, 20)}"
```
User defined function using the parameters "ip" & "rules" within a loop to 
```Python
def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    # Loop through each firewall rule and action in the dictionary
    for rule_ip, action in rules.items():
        # If the IP matches a rule IP, return the specified action
        if ip == rule_ip:
            return action
    # Default action is "allow" if the IP address does not match any firewall rules
    return "allow"
```
Where the main function of the script starts
```Python
def main():
    # Define the firewall rules with IP addresses as keys and actions (block or allow) as values
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }
```
```Python
    # Simulate network traffic by generating random IP addresses
    for _ in range(12):  # Loop 12 times to simulate 12 traffic events
        ip_address = generate_random_ip()  # Generate a random IP address
        action = check_firewall_rules(ip_address, firewall_rules)  # Check if the IP matches any firewall rule
        random_number = random.randint(0, 9999)  # Generate a random number between 0 and 9999 to simulate traffic data
        # Print the IP address, action (block or allow), and random number for each traffic event
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")
```
Guards against other scripts calling or importing this one by forcing it to be executed directly.
```Python 
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
```
