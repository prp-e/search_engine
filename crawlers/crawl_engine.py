from bs4 import BeautifulSoup
import json 
import requests
import sys 

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
        #"description": description
    }

    if depth == 0:
        return 

    links = content.findAll('a')

    for link in links:
        try:
            if 'http' in link['href']:
                print(json.dumps(result, indent=2))
                crawl(link['href'], depth - 1)
        except KeyError as e:
            print(e)

# if __name__ == "__main__":
#     url = "http://en.wikipedia.org/wiki"
#     crawl(url, 5)