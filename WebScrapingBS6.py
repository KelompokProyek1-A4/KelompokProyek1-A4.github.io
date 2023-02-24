import requests
import os
import json
from bs4 import BeautifulSoup
res = []

os.system('cls')

URL = "https://www.cnnindonesia.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
popularHeadline = soup.find(class_="headline__terpopuler-list")

title = popularHeadline.find_all("h2", class_="title")
canal = popularHeadline.find_all("span", class_="kanal")

for i in range(len(title)):
    res.append({"id" : i+1, "title" : title[i].text.strip(), "canal" : canal[i].text.strip()})

JsonRes = json.dumps(res)
JsonFile = open("BSDatabase.json", "w")
JsonFile.write(JsonRes)
JsonFile.close()