#!/usr/bin/env python3

def get_number():
    
    while True:
        try:
            string = input("Give me a number: ")
            n = float(string)
            return n
        except ValueError:
            pass


def main():
    n = get_number()
    n.is_integer()
    if n.is_integer() == True:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

if __name__ == "__main__":
    main()