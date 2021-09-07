import newspaper
import requests
from bs4 import BeautifulSoup
#import random
from time import sleep
import re

def nor_web():
    n_paper = newspaper.build(site, memoize_articles=False)
    #with open('data1.txt', mode='w+') as file:
    for article in n_paper.articles:
        try:
            print(article.url)
            article = newspaper.Article(article.url)
            article.download()
            article.parse()
            print('Tiêu đề:',article.title.strip())
            print('Mô tả:',article.meta_description)
            print("<=======================================================================>" + '\n')
            file.write("Link:       " + article.url + '\n')
            file.write('Tiêu đề:    ' + article.title.strip()+'\n')
            file.write('Mô tả:      ' + article.meta_description + '\n')
            file.write("<=======================================================================>" + '\n \n')
        except:
            continue
    #        file.write(article.url+'\n')

def kenh14():
    try:
        response = requests.get("https://kenh14.vn/")
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.findAll('h3', class_='knswli-title')
        links = [link.find('a').attrs["href"] for link in titles]
        for link in links:
            print("https://kenh14.vn"+link)
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
                print("Mô tả: " + abstract.strip())
            #print("Nội dung: " + content)
            #print("Ảnh minh họa: " + image)
                print("<=======================================================================>" + '\n')
                file.write("Link:       https://kenh14.vn"+ link + '\n')
                file.write("Tiêu đề:    " + title +'\n')
                file.write("Mô tả:      " + abstract.strip() + '\n')
                file.write("<=======================================================================>" + '\n \n')
            #sleep(random.randint(1,2))
    except:
        print('')

def main():
    global site
    global file
    site = input('Insert website: ')
    try:
        name = re.search('://(.*?)/', site).group(1)
    except AttributeError:
        name = site
    with open(name + '.txt', mode='w+', encoding='utf-8') as file:
        if 'kenh14' in site:
            kenh14()
        else:
            nor_web()
    cont = input('Do you want to continue? (Y/N) ')
    if cont in ['', 'Y', 'y']:
        main()
    else:
        print('{:=^51}'.format('Programmed by Trần Thanh Hùng'))
        print('{:=^51}'.format('Contact for work: fb.com/darrenhtth'))
        print('{:=^51}'.format('Thanks for using'))
        sleep(3)
        exit(0)

print('{:=^51}'.format('Programmed by Trần Thanh Hùng'))
print('{:=^51}'.format('Contact for work: fb.com/darrenhtth'))
print('{:=^51}'.format('Press Ctrl+C to stop!'))
try:
    main()
except KeyboardInterrupt:
    print('{:=^51}'.format('Programmed by Trần Thanh Hùng'))
    print('{:=^51}'.format('Contact for work: fb.com/darrenhtth'))
    print('{:=^51}'.format('Thanks for using'))
    sleep(3)
    exit(0)