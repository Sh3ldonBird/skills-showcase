## First
#def main():
#    name = input("What's your name? ")
#    hello(name)
#
#def hello(to="world"):
#    print("hello,", to)
#
#if __name__ == "__main__":
#    main()

## Second/Third
def main():
    name = input("What's your name? ")
    #output = hello(name)
    #print(output)
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()