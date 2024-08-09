#!/usr/bin/env python3

def change_char(str):
    result = ""
    for char in str:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

def main():
    string = input("")
    new_string = change_char(string)
    print(new_string)

if __name__ == "__main__":
    main()