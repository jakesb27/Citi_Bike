import os
import requests
import zipfile
from bs4 import BeautifulSoup

url = 'https://s3.amazonaws.com/tripdata/'

response = requests.get(url)
soup = BeautifulSoup(response.text, features='xml')
files = soup.find_all('Key')


def download_zip(zip_name):
    zip_url = url + zip_name

    with open(zip_name, 'wb') as f:
        resp = requests.get(zip_url)
        f.write(resp.content)

    with zipfile.ZipFile(zip_name, 'r') as zip_file:
        zip_file.extractall(f"resources")

    os.remove(zip_name)


"""File format changes starting with 2021-02"""
"""Scrape files only from 2023"""
for i in range(len(files) - 1):
    try:
        name = int(files[i].get_text()[:6])
        if 202304 < name > 202212:
            download_zip(files[i].get_text())
    except ValueError:
        pass

dir_path = 'resources/__MACOSX'

for file in os.listdir(dir_path):
    os.remove(f'{dir_path}/{file}')

os.rmdir(dir_path)
