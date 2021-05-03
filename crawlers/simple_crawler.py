from bs4 import BeautifulSoup
import requests

url = 'https://www.farsnews.ir'

response = requests.get(url) 
content = BeautifulSoup(response.text, 'lxml')

links = content.findAll('a')
for link in links:
    if 'http' not in link['href']:
        link = url + link['href']
        res = requests.get(link)
        content = BeautifulSoup(res.text, 'lxml')
        title = content.find('title')

        print({'link' : link, 'title' : title.text})
    else:
        link = link['href']
        res = requests.get(link)
        content = BeautifulSoup(res.text, 'lxml')
        title = content.find('title')

        print({'link' : link , 'title' : title.text})