# # n = 0

# # while n < 3:
# #     print("meow")
# #     n += 1

# # the _ variable is not used by the user/human. It is only requisite to run a specific functionality in python.
# for _ in range(3):
#     print("meow")

# print("meaow\n"* 3, end="")

def main():
    make_me_meow(x="")

def make_me_meow(x):
    while True:
        x = int(input("What\'s x? "))
        if x > 0:
            break
    for _ in range(x):
        print("Meow")

main()
