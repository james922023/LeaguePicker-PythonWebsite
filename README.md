# WHAT IS THIS APP?
This app will be a league of legends Champions picker.

# What does it do?
This app will randomly select a champion to play, based on a selected role.

# How Does this work?
I will have a database with preset champions, items, skillorders, and runes the way I would play them. Upon clicking the button, it will show everything in the order I would like it as an assistnace to building my character the way I normally do it, so I dont have to think.

# Updates

6/27/2025 - Basic View Created

![image](https://github.com/user-attachments/assets/465ba9e2-35c6-471e-972d-1f2e894d453d)

currently, its a django app that uses sqlite and a simple index.html view was made. I Plan to use React from now on.

6/27/2025 - Added Basic React & Docker

![image](https://github.com/user-attachments/assets/c3769899-60cb-4e71-ae91-df3e1ef5c43d)

currently, its just the react vite template.

![image](https://github.com/user-attachments/assets/98a11e8b-52c2-4a69-98ae-acdbd1eecc2d)

I also added docker. Note, had to change port in dockerfilee to the matching one in the url for react, but also add to vite.config.ts code to allow the server to talk to docker and also list port there.

6/29/2025 - WebScraped Item names and added them to database

![image](https://github.com/user-attachments/assets/61e084c9-0cdf-45f4-9b7e-fe06f4c3ccd3)

As you can see, the items were added sucessfully. Before, I made the url /items run a function that takes all of the league items from the database, and then serializes them, returning a JSON for easier viewing and manipulation. I messed around with beautiful soup in an ipynb, and then once I grabbed what I wanted, I just made a python script without all of the print statements that scrapes from leagueoflegendswiki. If I ever want to updata the database with new items added, all I need to do is run that script and it will pull any new items and add them to the database. Next step is to scrape corresponding images, and have those display sucessfully.

7/1/2025 - webscraped item images and worked on roles page
![image](https://github.com/user-attachments/assets/01aff785-873f-429b-99e8-5a81d49b4d24)

This is the roles page right now. I scraped these small images, along with updating the previous item script to download the images of the items. The next step is to eedit the sprites to make them slightly larger, without distortion, and then format the page like the red lines in the image above. After the role page is done, I will work on grabbing all of the items, and figuring out how I should store those and rerieve them.

