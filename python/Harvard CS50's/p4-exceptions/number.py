## First
#try:
#    x = int(input("What's x? "))
#    print(f"x is {x}")
#except ValueError:
#    print("x is not an integer")
#
#print(f"x is {x}")

## Second
#try:
#    x = int(input("What's x? "))
#except ValueError:
#    print("x is not an integer")
#else:
#    print(f"x is {x}")

## Third
#while True:
#    try:
#        x = int(input("What's x? "))
#    except ValueError:
#        print("x is not an integer")
#    else:
#        break
#    
#print(f"x is {x}")

## Fourth
#def main():
#    x = get_int()
#    print(f"x is {x}")
#
#def get_int():
#    try:
#        x = int(input("What's x? "))
#        print(f"x is {x}")
#    except ValueError:
#        print("x is not an integer")
#    else:
#        #break
#        return x
#
#main()

## Fifth
#def main():
#    x = get_int()
#    print(f"x is {x}")
#def get_int():
#    while True:
#        try:
#            return int(input("What's x? "))
#        except ValueError:
#            pass
#
#main()

## Sixth
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()