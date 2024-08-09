#!/usr/bin/env python3

class MachuPichu:    
    def upcase_it(self, string):
        return string.upper()
    
def main():
    obj = MachuPichu()
    print(obj.upcase_it("hello"))

if __name__ == "__main__":
    main()