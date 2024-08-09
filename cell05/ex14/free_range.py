#!/usr/bin/env python3
import sys

def main():
    
    argc = len(sys.argv) - 1
    if argc != 2:
        print("none")
        sys.exit()
    number_1 = int(sys.argv[1])
    number_2 = int(sys.argv[2])
    array = list(range(number_1, number_2))
    print(array)

if __name__ == "__main__":
    main()
