#!/usr/bin/env python3

import sys

def get_string():
    string = input("What you gotta say? : ")
    if string == "STOP":
        exit()

def the_loop():
    while True:
        string = input("I got that! Anything else? : ")
        if string == "STOP":
            exit()

def main():
    get_string()
    the_loop()

if __name__ == "__main__":
    main()
        
