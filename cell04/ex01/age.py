#!/usr/bin/env python3

def get_number():

    while True:
        try:
            string = input("Please tell me your age: ")
            n = int(string)
            return n
        except ValueError:
            pass

def the_loop(n):
    print(f"You are currently {n} years old.")
    i = 10
    while i <= 30:
        print(f"In {i} years, you'll be {i + n} old.")
        i += 10

def main():
    number = get_number()
    the_loop(number)

if __name__ == "__main__":
    main()