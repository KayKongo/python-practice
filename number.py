def get_int(prompt):
    while True:
        try: # defensively prepare for exceptions
            return int(input(prompt))
        except ValueError: # if there is a ValueError
            print("x is not an integer. Try again!")
            # pass

def main():
    x = get_int("Enter an integer: ")
    print(f"x is {x}")

main()
