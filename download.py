#/Users/emmywonder

import requests
from bs4 import BeautifulSoup
import os

def download_file(url, folder):
    local_filename = url.split('/')[-1]
    path = os.path.join(folder, local_filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def main(url, download_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # You need to inspect the webpage to find the common pattern for audio files
    # This example assumes they are contained in <a> tags with a specific class or property
    audio_links = soup.find_all('a', href=True)  # Adjust this line based on the actual pattern

    for link in audio_links:
        href = link['href']
        if href.endswith('.mp3'):  # Check if the link is an audio file
            print(f'Downloading {href}...')
            download_file(href, download_folder)
            print(f'Finished downloading {href}')

if __name__ == '__main__':
    url = 'https://www.livingwordmedia.org/teachings/the-law-in-genesis-series-9a/'
    download_folder = '/Users/emmywonder/Downloads'  # Change this to your desired folder
    main(url, download_folder)

