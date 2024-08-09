#!/usr/bin/env python3

def get_string():
    
    while True:
        try:
            string = input("Give me a word: ")
            if string:
                return string
        except:
            pass

def main():
    low = get_string()
    up = low.upper()
    print(up)

if __name__ == "__main__":
    main()