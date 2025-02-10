#https://docs.python.org/3/howto/regex.html#regex-howto
#https://docs.python.org/3/library/re.html


#! /usr/bin/env python3

# Python libraries for regular expressions, csv's, and system file I/O
import re
import csv
import sys

# Empty lists for log levels
# Change to dictionaries??
error = []
warning = []

with open("/home/sheldon/github/skills-showcase/python/log-parsing/JSON-files/?/log1.txt", "r") as f:
    for line in f.readlines():
        result = re.search (r"\w*level=(warning|error)*[\w]*[\=\"\w\.][fF]ailed", line)
        if result != None:
            if result[1] == 'error':
                error.append(line)
            if result[1] == 'warning':
                warning.append(line)

with open('/home/sheldon/github/skills-showcase/python/log-parsing/JSON-files/?/error_message.txt', 'w', newline='') as error_list:
    error_list.writelines("%s\n" % x for x in error)  

with open('/home/sheldon/github/skills-showcase/python/log-parsing/JSON-files/?/warning_message.txt', 'w+', newline='') as warning_list:
    warning_list.writelines("%s\n" % y for y in warning)