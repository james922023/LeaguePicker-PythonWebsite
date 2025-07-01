from bs4 import BeautifulSoup
import requests
import os

url = 'https://wiki.leagueoflegends.com/en-us/Item'

league_wiki=requests.get(url)

soup=BeautifulSoup(league_wiki.text, features='html.parser')

soup.find('div', id='item-grid')

item_grid=soup.find('div', id='item-grid')

itemsection = item_grid.find_all('div',class_='item-icon')
    
scraped_names={}
for item in itemsection:
    item1 = item.get('data-item')
    temp=item.find_all('img')
    for img in temp:
        temp2=img.get('src')
        temp2="https://wiki.leagueoflegends.com/"+temp2
        temp2=temp2[0:-6]
        #print(temp2)  #item URL
    #print(item1)   #item name
    scraped_names[item1]=temp2


for key, url in scraped_names.items():
    if os.path.exists('./../react-frontend/public/images/items/'+key):
        print(f"File {key} already exists, skipping download.")
        continue
    try:
        
        response = requests.get(url)
        response.raise_for_status()
        with open('./../react-frontend/public/images/items/'+key, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {key}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
import re     
import os
urls='./../react-frontend/public/images/items/'
folder=os.listdir(urls)
for file in folder:
    if  not re.search('.png',file):
        os.rename(urls+file,urls+file+'.png')
    else:
        print('already png')   
    
