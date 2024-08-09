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
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")

if __name__ == "__main__":
    main()