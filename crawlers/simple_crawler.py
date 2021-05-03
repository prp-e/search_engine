from bs4 import BeautifulSoup
import requests

url = 'https://www.farsnews.ir/'

response = requests.get(url) 
content = BeautifulSoup(response.text, 'lxml')

links = content.findAll('a')
for link in links:
    print(link['href'])