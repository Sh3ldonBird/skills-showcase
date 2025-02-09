## First
#names = []
#
#for _ in range (3):
#    names.append(input("What's your name?"))
#
#for name in sorted(names):
#    print(f"hello, {name}")

## Second
#name = input("What's your name? ")
#
#file = open("names.txt", "w")
#file.write(name)
#file.close()

## Third
#name = input("What's your name? ")
#
#file = open("names.txt", "a")
#file.write(name)
#file.close()

## Fourth
#name = input("What's your name? ")
#
#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

## Fifth
#name = input("What's your name? ")
#
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

## Sixth
#with open("names.txt", "r") as file:
#    lines = file.readlines()
#
#for line in lines:
#    print("hello,", line.rstrip())

## Seventh
#with open("names.txt", "r") as file:
#    for line in file:
#        print("hello,", line.rstrip())

## Eighth
#names = []
#
#with open("names.txt") as file:
#    for line in file:
#        names.append(line.rstrip())
#
#for name in sorted(names):
#    print(f"hello, {name}")

# Ninth
#with open("names.txt") as file:
#    for line in sorted(file):
#        print("hello,", line.rstrip())

# Tenth
#names = []
#
#with open("names.txt") as file:
#    for line in file:
#        names.append(line.rstrip())
#
#for name in sorted(names, reverse=True):
#    print(f"hello, {name}")

## Eleventh


