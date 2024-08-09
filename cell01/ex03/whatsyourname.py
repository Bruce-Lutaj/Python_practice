
def get_name():
    while True:
        try:
            string = input("Hey, what's your first name? : ")
            if string:
                return string
        except:
            pass

def get_last_name():
    while True:
        try:
            string = input("Hey, what's your last name? : ")
            if string:
                return string
        except:
            pass

def main():
    first_name = get_name()
    last_name = get_last_name()
    whole_name = first_name + " " + last_name + "."
    print("Well, pleased to meet you,", whole_name)

if __name__ == "__main__":
    main()