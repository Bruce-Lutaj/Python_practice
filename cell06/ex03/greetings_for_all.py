#!/usr/bin/env python3
import sys

class Greet:
    def greetings(self, person = 'noble stranger'):
        if isinstance(person, str):
            print(f"Hello, {person}.")
        else:
            print("Error! It was not a name.")

def main():
    obj = Greet()
    obj.greetings('Alexandra')
    obj.greetings('Wil')
    obj.greetings()
    obj.greetings(42)

if __name__ == "__main__":
    main()