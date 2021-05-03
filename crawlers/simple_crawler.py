from bs4 import BeautifulSoup
import json 
import requests

url = 'https://www.farsnews.ir'

response = requests.get(url) 
content = BeautifulSoup(response.text, 'lxml')

links = content.findAll('a')
paragraphs = content.findAll('p')

description = ' '
for paragraph in paragraphs:
    description += paragraph.text.strip().replace('\n', ' ')

result = {
    'link' : url, 
    'links_found': len(links),
    'description': description
}

print(json.dumps(result, indent=2))
# for link in links:
#     if 'http' not in link['href']:
#         link = url + link['href']
#         res = requests.get(link)
#         content = BeautifulSoup(res.text, 'lxml')
#         title = content.find('title')

#         print({'link' : link, 'title' : title.text})
#     else:
#         link = link['href']
#         res = requests.get(link)
#         content = BeautifulSoup(res.text, 'lxml')
#         title = content.find('title')

#         print({'link' : link , 'title' : title.text})