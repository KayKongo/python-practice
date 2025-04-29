import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("You\'re so pretty " + sys.argv[1] + "!")