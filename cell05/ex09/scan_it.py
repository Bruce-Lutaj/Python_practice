#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc != 2:
        print("none")
        sys.exit()
    count = sys.argv[2].count(sys.argv[1])
    if count > 0:
        print(count)
    else:
        print("none")

if __name__ == "__main__":
    main()