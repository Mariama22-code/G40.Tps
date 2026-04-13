import urllib.request
import json

ville = input("Entrez le nom d'une ville : ")

cle_api = "09cb5a4e46ac239b54b797c58d887ddc"

url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle_api}&units=metric&lang=fr"

reponse = urllib.request.urlopen(url)
donnees = json.loads(reponse.read())

print("Ville :", donnees["name"])
print("Température :", donnees["main"]["temp"], "°C")
print("Description :", donnees["weather"][0]["description"])