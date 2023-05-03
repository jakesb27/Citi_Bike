import os
import requests
import zipfile
from bs4 import BeautifulSoup

url = 'https://s3.amazonaws.com/tripdata/'

response = requests.get(url)
soup = BeautifulSoup(response.text, features='xml')
files = soup.find_all('Key')


def download_zip(f_type, file):
    zip_url = url + file

    with open(file, 'wb') as f:
        response = requests.get(zip_url)
        f.write(response.content)

    with zipfile.ZipFile(file, 'r') as zip_file:
        zip_file.extractall(f"resources/{f_type}")

    os.remove(file)


"""File format changes starting with 2021-02"""
for i in range(len(files) - 1):
    try:
        name = int(files[i].get_text()[:6])
        if name > 202101:
            print("new", files[i].get_text())
            download_zip("new", files[i].get_text())
        else:
            print("old", files[i].get_text())
            download_zip("old", files[i].get_text())
    except ValueError:
        pass
