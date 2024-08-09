#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc != 1:
        print("none")
        sys.exit()
    string = sys.argv[1].lower()
    print (string)

if __name__ == "__main__":
    main()