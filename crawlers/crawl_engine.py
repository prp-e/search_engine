from bs4 import BeautifulSoup
import requests

def crawl(url, depth, results):
    try:
        response = requests.get(url)
    except:
        print(f"Failed to crawl {url}")

    content = BeautifulSoup(response.text, 'lxml')

    try:
        title = content.find('title').text 
        description = ''

        for tag in content.findAll('p'):
            description += tag.text.strip().replace('\n', ' ')
    except:
        return

    
    result = {
        "url": url, 
        "title": title, 
        "description": description
    }

    results.append(result)
    if depth == 0:
        return 

    links = content.findAll('a')

    for link in links:
        if 'http' in link['href']:
            print(link['href'])
            crawl(link['href'], depth - 1)
