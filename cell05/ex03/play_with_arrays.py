#!/usr/bin/env python3

def print_number(array):
    
    print("[", end="")
    for i in range(0, (len(array) - 1)):
        print(f"{array[i]}, ", end="")
    print(f"{array[i + 1]}]")


def add_number(array):

    n = 2
    new_list = []
    for i in array:
        new_list.append(i + n)
    return new_list

def create_new(array):
    
    result = add_number(array)
    new_list = []
    for i in result:
        if i >= 10:
            new_list.append(i)
    return new_list

def create_set(array):
    
    my_set = set()
    for i in array:
        my_set.add(i)
    return my_set


def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    print_number(array)
    array = create_new(array)
    new_set = create_set(array)
    print(new_set)
    

if __name__ == "__main__":
    main()