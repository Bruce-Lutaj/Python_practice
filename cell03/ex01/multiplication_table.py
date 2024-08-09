#!/usr/bin/env python3

def get_number():

    while True:
        try:
            string = input("Enter a number:\n")
            n = float(string)
            return n
        except ValueError:
            pass

def int_or_float(n):
    if n.is_integer():
        return int(n)
    return n

def the_loop(number, mult):
    while mult < 10:
       result = number * mult
       print(f"{mult} x {number} = {result}")
       mult += 1


def main():
    number = get_number()
    number = int_or_float(number)
    the_loop(number, 0)

if __name__ == "__main__":
    main()