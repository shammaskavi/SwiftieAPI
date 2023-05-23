import requests
import random


response = requests.get("http://127.0.0.1:8000/")
response.raise_for_status()

data = response.json()
print(data[random.randint(0, 6)]['lyric'])
