score = int(input("Enter your Score: "))

def check_grade(score=0):
    if score >= 90:
        print(f"Your score: {score} is an A!")
    elif score >= 80:
        print(f"Your score: {score} is a B!")
    elif score >= 70:
        print(f"Your score: {score} is a C!")
    elif score >= 60:
        print(f"Your score: {score} is a D!")
    elif score >= 50:
        print(f"Your score: {score} is an E!")
    else:
        print(f"Your score: {score} isn\'t great and you need to take the test again!")


def main():
    check_grade(score)

main()