import requests
import os
from urllib.parse import urlparse, unquote
from download_picture import download_picture


def extract_format_from_link(link):
    decoding_link = unquote(link)
    parse_link = urlparse(decoding_link)
    path, fullname = os.path.split(parse_link.path)
    format_path = os.path.splitext(fullname)
    file_name, format = format_path
    return format, file_name


def nasa_get(count_nasa, api_key):
    payload = {
        "api_key": api_key,
        "count": count_nasa,
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()
    images_json = response.json()
    for image_json in images_json:
        if image_json.get("media_type") == "image":
            if image_json.get("hdurl"):
                url_photos = image_json["hdurl"]
            else:
                url_photos = image_json["url"]
            format, file_name = extract_format_from_link(url_photos)
            path = os.path.join("images", f"{file_name}{format}")
            download_picture(url_photos, path, params=payload)


def main():
    count_nasa = 30
    api_key = os.environ['NASA_TOKEN']
    nasa_get(count_nasa, api_key)


if __name__ == "__main__":
   main()
    
