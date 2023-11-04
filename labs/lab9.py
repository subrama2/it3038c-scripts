import json
import requests



url = "http://localhost:3000/" 

response = requests.get(url)

if response.status_code == 200:
	widgetData = response.json()

print("widget list")
for widget in widgetData:
	print(f"Name: {widget['name']} is {widget['color']}")
else:
	print("failed to fetch data")
