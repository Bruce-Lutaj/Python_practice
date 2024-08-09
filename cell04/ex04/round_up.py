#!/usr/bin/env python3

import math

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
    ceil_n = math.ceil(n)
    print(ceil_n)

if __name__ == "__main__":
    main()