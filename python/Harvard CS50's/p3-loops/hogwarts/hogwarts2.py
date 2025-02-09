# Lists
#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

#outright print
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])

for student in students:
    print(student, students[student], sep=", ")