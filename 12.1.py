import json
import requests


url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        print(json_response['value'])
    else:
        print("Vitsin hakeminen epäonnistui. Yritä uudelleen.")
except requests.exceptions.RequestException as e:
    print("Virhe pyynnön suorittamisessa:", e)
