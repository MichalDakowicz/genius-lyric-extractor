import requests
from bs4 import BeautifulSoup

with open("lyrics.txt", "w", encoding='utf-8') as file:
    file.write("")

url = input("Enter the URL of Genius song website: ")

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

lyrics_containers = soup.find_all("div", attrs={"data-lyrics-container": "true"})

for lyrics_container in lyrics_containers:
    with open("lyrics.txt", "a", encoding='utf-8') as file:
        lyrics = str(lyrics_container)
        lyrics = lyrics.replace("<br/>", "\n")
        lyrics_filtered = ""
        in_tag = False
        for char in lyrics:
            if char == "<":
                in_tag = True
            elif char == ">":
                in_tag = False
                continue
            if not in_tag:
                lyrics_filtered += char
        file.write(lyrics_filtered)