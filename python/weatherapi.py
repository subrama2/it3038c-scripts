import json
import re
import requests


print("please enter your zip code: ")
zip = input()

apikey = "6bef96b9aff9835db2f05856b0a85e83"
url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={apikey}" 

r = requests.get(url)
data = r.json()
print(data["weather"][0]["description"])