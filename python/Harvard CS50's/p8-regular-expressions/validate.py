## First
# email = input("What's your email? ").strip()
#
#if "@" in email and "." in email:
#    print("valid")
#else:
#    print("Invalid")

## Second
#email = input("What's your email? ").strip()
#
#username, domain = email.split("@")
#
#if username and "." in domain:
#    print("Valid")
#else:
#    print("Invalid")

## Third
#email = input("What's your email? ").strip()
#
#username, domain = email.split("@")
#
#if username and domain.endswith(".edu"):
#    print("Valid")
#else:
#    print("Invalid")

## Fourth
import re 

email = input("What's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")