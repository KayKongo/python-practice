# Python code to check if a number is even or odd (hence its mathematical name parity)

number = int(input("Guess a number: "))

def check_parity(number=0):
    if number%2 == 0:
        print("Your number is even!")
    else:
        print("Your number is odd!")

def main():
    check_parity(number)

main()