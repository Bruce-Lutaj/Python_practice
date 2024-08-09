#!/usr/bin/env python3

def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    print("[", end="")
    for i in range(0, (len(array) - 1)):
        print(f"{array[i]}, ", end="")
    print(f"{array[i + 1]}]")

if __name__ == "__main__":
    main ()