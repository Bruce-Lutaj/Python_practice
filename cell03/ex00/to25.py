#!/usr/bin/env python3

def get_number():

    while True:
        try:
            string = input("Enter a number less than 25\n")
            n = int(string)
            return n
        except ValueError:
            pass

def the_loop(number):
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1

def main():
    number = get_number()
    if number >= 25:
        print("Error")
    else:
        the_loop(number)

if __name__ == "__main__":
    main()