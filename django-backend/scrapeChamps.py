from bs4 import BeautifulSoup
import requests
import re
import os
import django
from PlaystylePicker.models import LeagueChamp

def scrapeChamps():
    champurl='https://wiki.leagueoflegends.com/en-us/Champion#List_of_champions'
    league_champs=requests.get(champurl)
    league_get=BeautifulSoup(league_champs.text, features='html.parser')
    champ_grid=league_get.find('ul' , class_='champion_roster')
    champs=champ_grid.find_all('img')

    dict_champs={}
    for champ in champs:
        url=champ.get('src')
        name=re.search('46px-.+_', url)
        temp=name.group()[5:-1]
        temp2='https://wiki.leagueoflegends.com'+url[:-6]
        dict_champs[temp]=temp2
        
    for key, url in dict_champs.items():
        strings=key
        if re.search('%27',key):
            strings=key
            strings=re.sub('%27','\'',strings)
        if os.path.exists('./../react-frontend/public/images/champs/'+strings+'.png'):
            print(f"File {strings} already exists, skipping download.")
            continue
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open('./../react-frontend/public/images/champs/'+strings+'.png', 'wb') as f:
                f.write(response.content)
            champ=LeagueChamp(name=strings, url='/images/champs/'+strings+'.png')
            champ.save()
            print(f"Downloaded and saved {strings} to database")
            
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    scrapeChamps()
            
