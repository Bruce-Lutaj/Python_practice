#!/usr/bin/env python3
import sys

def multi_table():
    number = 0
    mult = 0
    while number <= 10:
        print(f"Table of {number}:", end=" ")
        while mult <= 10:
            result = number * mult
            print(result, end=" ")
            mult += 1
        print("")
        mult = 0
        number += 1
        

def main():
    argc = len(sys.argv)
    if argc > 1:
        print("none")
        sys.exit()
    multi_table()

if __name__ == "__main__":
 main()
    