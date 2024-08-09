#!/usr/bin/env python3
import sys

def main():

    suffix = "ism"
    argc = len(sys.argv) - 1
    if argc == 0:
        print("none")
        sys.exit()
    for i in sys.argv[1:]:
        if i.endswith(suffix):
            pass
        else:
            print(i + "ism")

if __name__ == "__main__":
    main()