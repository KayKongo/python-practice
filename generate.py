import random

# random.choice()
# def get_coin_toss():
#     return random.choice(["heads", "tails"])

# def main():
#     if get_coin_toss() == "heads":
#         print('You won!')
#     else:
#         print("You lost")

# main()


# random.randint()
# number = random.randint(1, 10)
# print(number)


# random.shuffle()
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)