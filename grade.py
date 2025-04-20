score = int(input("Enter your Score: "))

def check_grade(score=0):
    if 90 <= score <= 100:
        print(f"Your score: {score} is an A!")
    elif 80 <= score <= 89:
        print(f"Your score: {score} is a B!")
    elif 70 <= score <= 79:
        print(f"Your score: {score} is a C!")
    elif 60 <= score <= 69:
        print(f"Your score: {score} is a D!")
    elif 50 <= score <= 59:
        print(f"Your score: {score} is an E!")
    else:
        print(f"Your score: {score} isn\'t great and you need to take the test again!")


def main():
    check_grade(score)

main()