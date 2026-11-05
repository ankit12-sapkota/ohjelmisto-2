import requests
import json

request = "https://api.chucknorris.io/jokes/random/"

try:
    response = requests.get(request)
    if response.status_code==200:
        response = response.json()
        print("Joke", response["value"])
    else:
        print("No joke found.")

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")


