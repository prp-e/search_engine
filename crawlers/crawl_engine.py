from bs4 import BeautifulSoup
import json 
import requests
import sys 

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
            try:
                print(link['href'])
                crawl(link['href'], depth - 1, results)
            except KeyError as e:
                print(e)

if __name__ == "__main__":
    url = "http://en.wikipedia.org/wiki"
    results = []
    crawl(url, 5, results)

    with open('results.json', 'w') as j: 
        j.write(json.dumps(results, indent=2))
