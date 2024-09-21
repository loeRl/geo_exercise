import requests
import json
import os
import time
from zipfile import ZipFile

class SwisstopoAccess:
    def __init__(self, base_url="https://data.geo.admin.ch/api/stac/v0.9"):
        self.base_url = base_url

    def get_collections(self):
        collections_url = f"{self.base_url}/collections"
        response = requests.get(collections_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch collections: {response.status_code}")
        return response.json()

    def browse_collections(self, collections):
        for index, collection in enumerate(collections['collections']):
            print(f"{index}: {collection['title']}")
            print(f"Description: {collection['description']}")
            print(f"ID: {collection['id']}")
            print(f"License: {collection['license']}")
            print("\n")

    def fetch_collection_items(self, collection_id):
        items_url = f"{self.base_url}/collections/{collection_id}/items"
        response = requests.get(items_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch collection items: {response.status_code}")
        return response.json()

    def download_assets(self, collection_name, items_metadata):
        base_dir = './data'
        collection_dir = os.path.join(base_dir, collection_name)
        os.makedirs(collection_dir, exist_ok=True)
        
        for feature in items_metadata['features']:
            for asset_name, asset_info in feature['assets'].items():
                asset_url = asset_info['href']
                asset_filename = os.path.join(collection_dir, asset_name)
                
                # Print message before downloading
                print(f"Starting download of {asset_name} from {asset_url}")
                
                # Download the asset
                try:
                    with requests.get(asset_url, stream=True) as response:
                        response.raise_for_status()
                        total_size = int(response.headers.get('content-length', 0))
                        downloaded_size = 0
                        with open(asset_filename, 'wb') as file:
                            for chunk in response.iter_content(chunk_size=8192):
                                if chunk:
                                    file.write(chunk)
                                    downloaded_size += len(chunk)
                                    print(f"Downloading {asset_name}: {downloaded_size}/{total_size} bytes", end='\r')
                    print(f"\nDownloaded {asset_name} to {asset_filename}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to download {asset_name} from {asset_url}: {e}")
                    continue  # Skip to the next asset if download fails
                
                # Unzip the file if it is a zip file
                if asset_filename.endswith('.zip'):
                    print(f"Unzipping {asset_filename}")
                    with ZipFile(asset_filename, 'r') as zip_ref:
                        zip_ref.extractall(collection_dir)
                    print(f"Unzipped {asset_filename}")
                    
                    # Delete the zip file after unzipping
                    os.remove(asset_filename)
                    print(f"Deleted {asset_filename}")
                else:
                    print(f"Skipping unzipping of {asset_filename}")
            
            print(f"Successfully downloaded all assets and unzipped all zip files for the collection: {collection_name}")
            
            # Waiting download timer
            print("Waiting for 5 seconds before the next download...")
            time.sleep(5)