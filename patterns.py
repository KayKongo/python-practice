def print_pattern1():
    length = int(input("How many rows and coloumns do you want to print? => "))

    for i in range(length):
        print("*" * length)

    # code to print the list of even numbers from 0 - 20
    # for _ in range(0, 21, 2):
    #     print(_)

def print_pattern2():
    length = int(input("How many steps do you want to print? => "))

    for i in range(1, length+1):
        for j in range(1, length+1):
            if i == j:
                print("*"*j)

def main():
    print_pattern2()

if __name__ == "__main__":
    main()