from bs4 import BeautifulSoup
import requests

def crawl(url, depth):
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

    return result