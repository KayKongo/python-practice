def main():
    name = input("What is your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()

# Ask the user for their name, remove whitespace from the name and capitalize the first letter of each of the user's names
# name = input("What is your name? ").strip().title()

# # Ask user for their age
# age = input("How old are you? ")

# # Split the user's name into first_name ana last_name
# first_name, last_name = name.split(" ")

# # Say hello to user and tell them their age
# print(f"Hello {first_name}! Your surname is {last_name} and It's so good to see you. You are {age} years old")


# """
# Nice job!
# You have successfully created a simple Python program that interacts with the user.
# """

# def main():
#     hello()
#     print("I defined the \"hello\" function after the main function and my code still works!")


# def hello(name="world"):
#     name = input("What's your name, handsome? ")
#     print(f"Hello {name}! I like you.")


# main()