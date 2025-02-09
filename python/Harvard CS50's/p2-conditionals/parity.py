""" 
x = int(input("What's x? "))

if x & 2 == 0:
    print("Even")
else:
    print("Odd")
"""
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

"""
# First iteration
def is_even(n):
    if n & 2 == 0:
        return True
    else:
        return False
"""
"""
# Second iteration
def is_even(n):
    return True if n % 2 == 0 else False
"""
# Third iteration
# boolean value returns of True or False are already
# inherent in the code. It's either True or False.
def is_even(n):
    return n & 2 == 0

main()