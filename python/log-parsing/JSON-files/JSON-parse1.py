#https://docs.python.org/3/howto/regex.html#regex-howto
#https://docs.python.org/3/library/re.html

#! /usr/bin/env python3

import re
import csv
import sys

error = []
warning = []

with open(source_file, "r") as f:
    for line in f.readlines():
        result = re.search (r"\w*level=(warning|error)*[\w]*[\=\"\w\.][fF]ailed", line)
        if result != None:
            if result[1] == 'error':
                error.append(line)
            if result[1] == 'warning':
                warning.append(line)

with open('error_message.txt', 'w', newline='') as error_list:
    error_list.writelines("%s\n" % x for x in error)  

with open('warning_message.txt', 'w+', newline='') as warning_list:
    warning_list.writelines("%s\n" % y for y in warning)