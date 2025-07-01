from bs4 import BeautifulSoup
import requests


import os
import urllib.request

laneUrl= 'https://wiki.leagueoflegends.com/en-us/Category:Role_icons'

laneWiki=requests.get(laneUrl)
laneSoup=BeautifulSoup(laneWiki.text, features='html.parser')

mainContent=laneSoup.find('div',class_='mw-parser-output')
lanes=mainContent.find_all('p')
#print(lanes)

import re

LaneImages={}

for line in lanes:
    if "The official positions are " in line.get_text():
        foundImgs=line.find_all('img')
        for img in foundImgs:
            if img.has_attr('src'):
                src=img['src']
                src=src[0:-6]
                #print(src)
                name=re.search('/{1}.{,13}png/{1}',src)
                temp=name.group()
                temp2=temp[1:-1]
                LaneImages[temp2]="https://wiki.leagueoflegends.com"+src
                
#print(LaneImages)



for key, url in LaneImages.items():
    if os.path.exists('./../react-frontend/public/images/'+key):
        print(f"File {key} already exists, skipping download.")
        continue
    try:
        
        response = requests.get(url)
        response.raise_for_status()
        with open('./../react-frontend/public/images/'+key, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {key}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")