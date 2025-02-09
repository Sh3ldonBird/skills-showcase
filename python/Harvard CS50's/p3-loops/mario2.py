## First
#def main():
#    print_width(4)
#
#def print_row(width):
#    print("?" * width, end="")
## Second
def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()

main()

## Third
#def print_square(size):
#    for i in range(size):
#        print("#" * size)

## Fourth
#def main():
#    print_square(3)
#
#def print_square(size):
#    for i in range(size):
#        print_row(size)
#
#def print_row(width):
#    print("#" * width)
#
#main()