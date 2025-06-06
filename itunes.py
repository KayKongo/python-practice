import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Kindly specify the song you want to search for")

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# pretty_response = json.dumps(response.json(), indent=2)
# print(pretty_response)


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
obj = response.json()

for result in obj["results"]:
    print(result["trackName"])