#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc == 0:
        print("none")
    else:
        print(f"{sys.argv[1]}")

if __name__ == "__main__":
    main()