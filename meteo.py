import os 
import requests

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")

ville = input("Entrez une ville : ")

url = f"https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": ville,
    "appid": api_key,
    "units": "metric",
    "lang": "fr"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    temperature = data["main"]["temp"]
    pays = data["sys"]["country"]
    
    print(f"La température actuelle à {ville}({pays}) est de {temperature}°C.")
else:
    print(f"Erreur : Impossible de trouver la ville (Code {response.status_code})")
