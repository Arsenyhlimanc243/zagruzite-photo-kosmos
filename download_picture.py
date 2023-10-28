import requests
import os


def download_picture(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    if not os.path.exists("images"):
        os.makedirs("images")
    with open(path, 'wb') as file:
        file.write(response.content)



