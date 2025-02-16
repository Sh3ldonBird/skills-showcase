#! /usr/bin/env python3

import re
import csv
import sys
 
#Creates an empty list wherein you can add your errors.
error = [] 
#Creates an empty list wherein you can add your warnings.
warning = [] 

#Opens and reads the source file in this case the given txt file.
with open(source_file, "r") as f:
#Reads all the lines.  
   for line in f.readlines(): 
       #Searches the line with the words "error" or “warning" and “fail”. Uses capturing group for conditionals.
       result = re.search(r"\w*level=(warning|error)*[\w ]*[\=\"\w \.]*[fF]ailed", line)
       if result != None:
          #If this particular capture group has the word "error"
          if result[1] == 'error':  
             #Add the line into the error list
             error.append(line)    
          #If this particular capture group has the word "warning"
    
          if result[1] == 'warning':
          #Add the line into the warning list. 
             warning.append(line)   
#Creates a new file with all the listed lines that have errors.
with open('error_message.txt', 'w', newline='') as error_list:
    error_list.writelines("%s\n" % x for x in error)  


#Creates a new file with all the listed lines that have failure warnings.
with open('warning_message.txt', 'w+', newline='') as warning_list:
    warning_list.writelines("%s\n" % y for y in warning)