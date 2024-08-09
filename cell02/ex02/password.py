#!/usr/bin/env python3

def main():
    password = "zaza"
    check = input("")
    
    if (check == password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()