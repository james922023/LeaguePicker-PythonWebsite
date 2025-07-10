from bs4 import BeautifulSoup
import requests
import os
import re     
from PlaystylePicker.models import LeagueItem

def scrapeItems():

    url = 'https://wiki.leagueoflegends.com/en-us/Item'

    league_wiki=requests.get(url)

    soup=BeautifulSoup(league_wiki.text, features='html.parser')

    soup.find('div', id='item-grid')

    item_grid=soup.find('div', id='item-grid')
    starterThroughTrinkets=item_grid.find_all(class_='tlist')[:3]
    boots=item_grid.find_all(class_='tlist')[4:6]
    legendaryItems=item_grid.find_all(class_='tlist')[7:9]
    item_section=starterThroughTrinkets+boots+legendaryItems


    scraped_names={}
    for item in item_section:
        temp=item.find_all('img')
        for img in temp:
            temp2=img.get('src')
            name=re.search('b/.+png/',temp2)
            temp2="https://wiki.leagueoflegends.com/"+temp2
            temp2=temp2[0:-6]
            item1=name.group()[2:-1]
            #print(temp2)
            #print(item1)
            scraped_names[item1]=temp2
        


    for key, url in scraped_names.items():
        strings=key
        if re.search('%27',key):
            strings=re.sub('%27','\'',strings)
        if os.path.exists('./../react-frontend/public/images/items/'+strings):
            print(f"File {strings} already exists, skipping download.")
            continue
        try:
            
            response = requests.get(url)
            response.raise_for_status()
            with open('./../react-frontend/public/images/items/'+strings, 'wb') as f:
                f.write(response.content)
                item=LeagueItem(name=strings, url='/images/items/'+strings)
                item.save()
            print(f"Downloaded {strings}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
    
if __name__ == "__main__":
    scrapeItems()