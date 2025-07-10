from bs4 import BeautifulSoup
import requests
import os
import re     
from PlaystylePicker.models import LeagueRune


def scrapeRunes():
    Rune_url='https://wiki.leagueoflegends.com/en-us/Rune'

    Rune_request=requests.get(Rune_url)
    Runes_get=BeautifulSoup(Rune_request.text, features='html.parser')

    Rune_grid=Runes_get.find('table')
    Rune_images=Rune_grid.find_all('img')
    #print(Rune_images)
    Runes_Dict={}
    for img in Rune_images:
        temp2=img.get('src')
        temp2=temp2[:-6]
        temp2='https://wiki.leagueoflegends.com'+temp2
        name=re.search('52px.+png',temp2)
        name=name.group()[5:]
        #print(temp2)
        #print(name)
        Runes_Dict[name]=temp2
        
    for key, url in Runes_Dict.items():
        if os.path.exists('./../react-frontend/public/images/runes/'+key):
            print(f"File {key} already exists, skipping download.")
            continue
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open('./../react-frontend/public/images/runes/'+key, 'wb') as f:
                f.write(response.content)
                item=LeagueRune(name=key, url='/images/runes/'+key)
                item.save()
            print(f"Downloaded {key}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    scrapeRunes()