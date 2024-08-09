#!/usr/bin/env python3
import sys

class Killer_B:
    
    def shrink(self, string):
         return string[:8]

    def enlarge(self, string):
        while len(string) < 8:
            string += "Z"
        return string

def main():
    obj = Killer_B()
    argc = len(sys.argv) - 1
    if argc == 0:
        print("none")
    else:
        for i in sys.argv[1:]:
            if len(i) > 8:
                print(obj.shrink(i))
            elif len(i) < 8:
                print(obj.enlarge(i))
            else:
                print(i)

if __name__ == "__main__":
    main()