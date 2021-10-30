from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import shutil

TRACKS_URL = "https://www.formula1.com/en/racing/2021.html"
FOLDER_NAME = "tracks_images"

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
html_content = requests.get(TRACKS_URL).text
soup = BeautifulSoup(html_content, "html.parser")

tracks_urls = soup.select('a.event-item-wrapper.event-item-link:not([href*="/article"]):not([href*="/Pre-Season"])')

# Remove folder if exists
if os.path.isdir(f'./{FOLDER_NAME}'):
    shutil.rmtree(f'./{FOLDER_NAME}')

# Creates folder
os.mkdir(FOLDER_NAME)

# Download driver images to the folder
for track_url in tracks_urls:
    uri = track_url.attrs['href']
    track_name = uri.split('/')[4].split('.')[0]
    full_track_url = f'https://www.formula1.com{uri}'

    new_html_content = requests.get(full_track_url).text
    new_soup = BeautifulSoup(new_html_content, "html.parser")

    track_image = new_soup.select('a[href*="/Circuit"] img.lazy')[0]
    track_image_url = track_image.attrs['data-src']
    urllib.request.urlretrieve(track_image_url, f'{FOLDER_NAME}/{track_name}.png')
