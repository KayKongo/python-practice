import sys
from sayings import hello
from sayings import goodbye


if len(sys.argv) == 2:
    name = sys.argv[1]
    hello(name)
    goodbye(name)