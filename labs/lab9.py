import json
from turtle import width
import requests



url = "http://localhost:3000/" 

response = requests.get(url)

if response.status_code == 200:
	widgetData = response.json()

print("widget list")
for widget in widgetData:
	print(f"Name: {width['name']} is {width['color']}")
else:
	print("failed to fetch data")
