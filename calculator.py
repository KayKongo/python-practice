# x = float(input("Choose a number between 1 -> 100: "))
# y = float(input("Choose a number between 1 -> 50: "))

# z = x / y

# # print out a properly formatted answer
# # print(f"{z:,}")
# print(f"{z:.4f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(value=0):
    return pow(value, 2)

main()