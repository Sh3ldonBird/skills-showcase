import random  # Import the random module to generate random numbers

def generate_random_ip():
    """Generate a random IP address."""
    # Create an IP address in the "192.168.1.x" range with a random last octet between 0 and 20
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    # Loop through each firewall rule and action in the dictionary
    for rule_ip, action in rules.items():
        # If the IP matches a rule IP, return the specified action
        if ip == rule_ip:
            return action
    # Default action is "allow" if the IP address does not match any firewall rules
    return "allow"

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

    # Simulate network traffic by generating random IP addresses
    for _ in range(12):  # Loop 12 times to simulate 12 traffic events
        ip_address = generate_random_ip()  # Generate a random IP address
        action = check_firewall_rules(ip_address, firewall_rules)  # Check if the IP matches any firewall rule
        random_number = random.randint(0, 9999)  # Generate a random number between 0 and 9999 to simulate traffic data
        # Print the IP address, action (block or allow), and random number for each traffic event
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
