## First
#with open("students.csv") as file:
#    for line in file:
#        row = line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")

## Second
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        print(f"{name} is in {house}")

# Third
#students = []
#
#with open ("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        students.append(f"{name} is in {house}")
#
#for student in sorted(students):
#    print(student)

## Fourth
#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {"name": name, "house": house}
#        #student = ["name"] = name
#        #student["house"] = houseline.strip()
#
#def get_name(student):
#    return student["name"]
#
#for student in sorted(students, key=get_name):
#    print(f"{student['name']} is in {student['house']}")

## Fifth
#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {"name": name, "house": house}
#        students.append(student)
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['house']}")

## Sixth
#students = []
#
#with open("students2.csv") as file:
#    for line in file:
#        name, home = line.rstrip().split(",")
#        student = {"name": name, "home": home}
#        students.append(student)
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")

# Seventh
#import csv
#
#students = []
#
#with open("students2.csv") as file:
#    reader = csv.DictReader(file)
#    for name, home in reader:
#        students.append({"name": name, "home": home})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")

# Eighth
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})