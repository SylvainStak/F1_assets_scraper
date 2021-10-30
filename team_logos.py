from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import shutil

TEAM_LOGOS_URL = "https://www.formula1.com/en/teams.html"
FOLDER_NAME = "team_logos_images"

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
html_content = requests.get(TEAM_LOGOS_URL).text
soup = BeautifulSoup(html_content, "html.parser")

logos = soup.select('div.logo img.lazy')

# Remove folder if exists
if os.path.isdir(f'./{FOLDER_NAME}'):
    shutil.rmtree(f'./{FOLDER_NAME}')

# Creates folder
os.mkdir(FOLDER_NAME)

# Download cars images to the folder
for logo in logos:
    logo_image_url = logo.attrs['data-src']
    team_name = logo_image_url.split('/')[8].split('.')[0]
    urllib.request.urlretrieve(logo_image_url, f'{FOLDER_NAME}/{team_name}.png')