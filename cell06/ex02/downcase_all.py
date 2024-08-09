#!/usr/bin/env python3
import sys

class MachuPichu:    
    def downcase_it(self, string):
        return string.lower()

def main():
    obj = MachuPichu()
    argc = len(sys.argv) - 1
    if argc == 0:
        print("none")
    else:
        for i in sys.argv[1:]:
            print(obj.downcase_it(i))

if __name__ == "__main__":
    main()