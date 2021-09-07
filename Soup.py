import requests
from bs4 import BeautifulSoup
import random
from time import sleep

response = requests.get("https://kenh14.vn/")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.findAll('h3', class_='knswli-title')
links = [link.find('a').attrs["href"] for link in titles]
for link in links:
    print(link)
    if 'http' in link:
        continue
    else:
        news = requests.get("https://kenh14.vn" + link)
        soup = BeautifulSoup(news.content, "html.parser")
        title = soup.find("h1", class_="kbwc-title").text
        abstract = soup.find("h2", class_="knc-sapo").text
    #body = soup.find("div", id="main-detail-body")
    #content = body.findChildren("p", recursive=False)[0].text +      body.findChildren("p", recursive=False)[1].text
    #image = body.find("img").attrs["src"]
        print("Tiêu đề: " + title)
        print("Mô tả: " + abstract.lstrip())
    #print("Nội dung: " + content)
    #print("Ảnh minh họa: " + image)
        print("_________________________________________________________________________")
    sleep(random.randint(1,4))
