from bs4 import BeautifulSoup

import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movetitles = soup.find_all(name="h3", class_ ="title")

#print(movetitles)

reverse = movetitles[::-1]



for i in reverse:
    k = i.text
    print(k)

    f = open("demofile2.txt", "a", encoding="UTF-8")

    w = f.write(f"{k}\n")

    f.close()