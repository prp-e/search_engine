from bs4 import BeautifulSoup
import json 
import requests

url = 'https://www.farsnews.ir/news/14000213000859/%D9%85%D9%82%D8%A7%D9%85-%D8%AF%D9%88%D9%84%D8%AA-%D8%AA%D8%B1%D8%A7%D9%85%D9%BE-%D8%A8%D8%A7%D8%B1%D9%87%D8%A7-%D8%AE%D9%88%D8%A7%D8%B3%D8%AA%D8%A7%D8%B1-%D9%88%D8%B3%D8%A7%D8%B7%D8%AA-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87-%D9%88-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3-%D8%A8%D8%B1%D8%A7%DB%8C-%D9%85%D8%B0%D8%A7%DA%A9%D8%B1%D9%87-%D8%A8%D8%A7'

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