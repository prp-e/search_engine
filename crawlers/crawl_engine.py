from bs4 import BeautifulSoup
import json 
import pymongo
import requests
import sys 

DB_CONNECTION = pymongo.MongoClient('mongodb://127.0.0.1:27017')
DB = DB_CONNECTION.search_results 
INDEXED_LINKS = DB.indexed_results 

def crawl(url, depth):
    try:
        print(f"crawling {url} in depth of {depth}")
        response = requests.get(url)
    except UnboundLocalError:
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

    INDEXED_LINKS.insert_one(result)
    INDEXED_LINKS.create_index(
        [
            ('url', pymongo.TEXT),
            ('title', pymongo.TEXT), 
            ('description', pymongo.TEXT)
        ]
    )

    if depth == 0:
        return 

    links = content.findAll('a')

    for link in links:
        try:
            if 'http' in link['href']:
                crawl(link['href'], depth - 1)

        except KeyError as e:
            pass