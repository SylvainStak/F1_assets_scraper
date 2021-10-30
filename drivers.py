from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import shutil

DRIVERS_URL = "https://www.formula1.com/en/drivers.html"
FOLDER_NAME = "drivers_images"

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
html_content = requests.get(DRIVERS_URL).text
soup = BeautifulSoup(html_content, "html.parser")

drivers = soup.select('div.listing-item--image-wrapper img:not([data-src*="/2018-redesign-assets/"])')

# Remove folder if exists
if os.path.isdir(f'./{FOLDER_NAME}'):
    shutil.rmtree(f'./{FOLDER_NAME}')

# Creates folder
os.mkdir(FOLDER_NAME)

# Download driver images to the folder
for driver in drivers:
    driver_image_url = driver.attrs['data-src']
    driver_name = driver_image_url.split('/')[8]
    urllib.request.urlretrieve(driver_image_url, f'{FOLDER_NAME}/{driver_name}.png')
