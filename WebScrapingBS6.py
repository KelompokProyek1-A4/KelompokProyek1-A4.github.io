import requests
import os
import json
from bs4 import BeautifulSoup
res = []

os.system('cls')

URL = "https://www.cnnindonesia.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
latest = soup.find(class_="l_content")

title = latest.find_all("h2", class_="title")
canal = latest.find_all("span", class_="kanal")
img = latest.find_all("img")
url = latest.find_all("a")

# print(latest)

link = [url['href'] for url in url]
imgurl = [img['src'] for img in img]

# print(link)

for i in range(len(title)):
    res.append({"id" : i+1, "title" : title[i].text.strip(), "canal" : canal[i].text.strip(), "img" : imgurl[i], "link" : link[i]})

# print(link[1])
JsonRes = json.dumps(res, indent=4)
JsonFile = open("BSDatabase.json", "w")
JsonFile.write(JsonRes)
JsonFile.close()