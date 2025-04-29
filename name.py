import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Yo! You forgot to add your first name in the CLI")

# Execute Code
for arg in sys.argv[1:]:
    print("Hello! My name is", arg)