from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import shutil

CARS_URL = "https://www.formula1.com/en/teams.html"
FOLDER_NAME = "cars_images"

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
html_content = requests.get(CARS_URL).text
soup = BeautifulSoup(html_content, "html.parser")

cars = soup.select('div.listing-image img.lazy')

# Remove folder if exists
if os.path.isdir(f'./{FOLDER_NAME}'):
    shutil.rmtree(f'./{FOLDER_NAME}')

# Creates folder
os.mkdir(FOLDER_NAME)

# Download cars images to the folder
for car in cars:
    car_image_url = car.attrs['data-src']
    team_name = car_image_url.split('/')[8].split('.')[0]
    urllib.request.urlretrieve(car_image_url, f'{FOLDER_NAME}/{team_name}.png')
