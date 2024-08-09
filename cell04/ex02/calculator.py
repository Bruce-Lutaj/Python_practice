#!/usr/bin/env python3

def get_first_number():

    while True:
        try:
            string = input("Give me the first number: ")
            n = float(string)
            return n
        except ValueError:
            pass

def get_second_number():

    while True:
        try:
            string = input("Give me the second number: ")
            n = float(string)
            return n
        except ValueError:
            pass
 
def int_or_float(n):
    if isinstance(n, int):
        return n
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

def the_calculator(n_1, n_2):
    print("Thank you!")
    print (f"{n_1} + {n_2} = {int_or_float(n_1 + n_2)}")
    print (f"{n_1} - {n_2} = {int_or_float(n_1 - n_2)}")
    print (f"{n_1} / {n_2} = {int_or_float(n_1 / n_2)}")
    print (f"{n_1} * {n_2} = {int_or_float(n_1 * n_2)}")

def main():
    n1 = get_first_number()
    n2 = get_second_number()
    n1 = int_or_float(n1)
    n2 = int_or_float(n2)
    the_calculator(n1, n2)

if __name__ == "__main__":
    main()