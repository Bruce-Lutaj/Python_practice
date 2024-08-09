#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc < 2:
        print("none")
        sys.exit()
    rev_argv = list(reversed(sys.argv[1:]))
    for i in rev_argv:
        print(i)

if __name__ == "__main__":
    main()