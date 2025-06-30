from bs4 import BeautifulSoup
import requests

url = 'https://wiki.leagueoflegends.com/en-us/Item'

league_wiki=requests.get(url)

soup=BeautifulSoup(league_wiki.text, features='html.parser')

soup.find('div', id='item-grid')

item_grid=soup.find('div', id='item-grid')

itemsection = item_grid.find_all('div',class_='item-icon')

scraped_names=[]
for item in itemsection:
    item1 = item.get('data-item')
    scraped_names.append(item1)
    #print(item1)
    
    
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from PlaystylePicker.models import LeagueItem

for name in scraped_names:
    LeagueItem.objects.get_or_create(name=name)  #add each scraped item to the database
    
print('done scrapin items! They were added to the database!')