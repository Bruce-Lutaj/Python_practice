#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc != 1:
        print("none")
        sys.exit()
    string = input("What was the parameter? ")
    if string == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()