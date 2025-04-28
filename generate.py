import random

def get_coin_toss():
    return random.choice(["heads", "tails"])

def main():
    if get_coin_toss() == "heads":
        print('You won!')
    else:
        print("You lost")

main()