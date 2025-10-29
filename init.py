import os
import glob
import requests
import pandas as pd

# List of Figshare article IDs
article_ids = [
    '11394819',
    '11394816',
    '11394804',
    '11394801',
    '11394792',
    '11394786',
    '11394783',
    '11394780',
    '11394768',
    '11394765',
    '11394657'
]

# Directory where files will be saved
save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database'))
os.makedirs(save_dir, exist_ok=True)

def sanitize_filename(file_name):
    """Remove 'GRF_' e 'PRO_' do nome do arquivo."""
    return file_name.replace("GRF_", "").replace("PRO_", "")

def download_file(file_url, file_name, save_path):
    response = requests.get(file_url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f'{file_name} downloaded')

def download_all():
    base_api_url = 'https://api.figshare.com/v2/articles/'
    
    print("Starting to download the files. Please wait...")
    for article_id in article_ids:
        # Get article metadata
        response = requests.get(f'{base_api_url}{article_id}')
        response.raise_for_status()
        article_metadata = response.json()

        # Check for files associated with the article
        files = article_metadata.get('files', [])
        if not files:
            print(f"No file found for article ID {article_id}")
            continue

        # Download each file associated with the article
        for file_info in files:
            original_file_name = file_info['name']
            sanitized_file_name = sanitize_filename(original_file_name)
            file_url = file_info['download_url']
            save_path = os.path.join(save_dir, sanitized_file_name)
            download_file(file_url, sanitized_file_name, save_path)

    print('\nAll files have been downloaded')

if __name__ == '__main__':
    download_all()
    print("\nNow you are ready to test the models!")
