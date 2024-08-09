#!/usr/bin/env python3

def get_number_one():

    while True:
        try:
            string = input("Enter the first number:\n")
            n = float(string)
            return n
        except ValueError:
            pass

def get_number_two():

    while True:
        try:
            string = input("Enter the second number:\n")
            n = float(string)
            return n
        except ValueError:
            pass

def main():
    n_1 = get_number_one()
    n_2 = get_number_two()
    result = n_1 * n_2
    print(f"{n_1} x {n_2} = {result}")
    if result < 0:
        print("This number is negative.")
    elif result > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

if __name__ == "__main__":
    main()
