#!/usr/bin/env python3
import sys

def main():

    argc = len(sys.argv) - 1
    if argc != 1:
        print("none")
        sys.exit()
    
    count = sys.argv[1].count('z')
    if count == 0:
        print("none")
    else:
        print('z' * count)

if __name__ == "__main__":
    main()