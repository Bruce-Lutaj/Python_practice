#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc == 0:
        print("none")
        sys.exit()
    print(f"parameters: {argc}")
    for i in sys.argv[1:]:
        print(f"{i}: {len(i)}")

if __name__ == "__main__":
    main()