#!/usr/bin/env python3
import sys

class Ruler_13:

    def add_one(self, value):
        value += 1
        return value

def main():
    obj = Ruler_13()
    num = 5
    print(num)
    print(obj.add_one(num))

if __name__ == "__main__":
    main()