#!/usr/bin/env python3

def get_number():

    while True:
        try:
            string = input("")
            n = float(string)
            return n
        except ValueError:
            pass

def main():
    number = get_number()
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

if __name__ == "__main__":
    main()
