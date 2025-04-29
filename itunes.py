import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Kindly specify the song you want to search for")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
