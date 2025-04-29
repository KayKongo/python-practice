import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Yo! You forgot to add your first name in the CLI")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments in the CLI. Gyae gyimie nu!")

# Execute Code
print("Hello! My name is", sys.argv[1])