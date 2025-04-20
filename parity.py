# Python code to check if a number is even or odd (hence its mathematical name parity)
def main():
    x = int(input("What\'s x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()
