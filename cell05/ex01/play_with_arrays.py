#!/usr/bin/env python3

def print_number(array):
    
    print("[", end="")
    for i in range(0, (len(array) - 1)):
        print(f"{array[i]}, ", end="")
    print(f"{array[i + 1]}]")

def create_new(array):

    n = 2
    new_list = []
    for i in array:
        new_list.append(i + n)
    return new_list

def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    print("Original array: ", end="") 
    print_number(array)
    new_arr = create_new(array)
    print("New array: ", end="")
    print_number(new_arr)

if __name__ == "__main__":
    main()