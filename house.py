def main():
    name = input("What\'s your name? ")
    get_house(name)

def get_house(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

main()