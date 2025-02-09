#url = input("URL: ").strip()
#
#username = url.replace("https://twitter.com/")
#print(f"Username: {username}")


## Second
## To get the twitter url
#url = input("URL: ").strip()
#
## To parse the users username from the full twitter url
#username = url.removeprefix("https://twitter.com/")
#print(f"Username: {username}")

## Third
#import re
#
#url = input("URL: ").strip()
#
#username = re.sub(r"https://twitter.com/", "", url)
#print(f"Username: {username}")

## Fourth - regular expressions to?
#import re
#
#url = input("URL: ").strip()
## Notate which regex symbols do what
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")

## Fifth
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))

