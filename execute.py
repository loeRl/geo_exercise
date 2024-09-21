from access_swisstopo import SwisstopoAccess

def main():
    # Initialize the SwisstopoAccess class
    swisstopo = SwisstopoAccess()

    # Get the collections
    collections = swisstopo.get_collections()

    # Browse the collections
    print("Browsing collections:")
    swisstopo.browse_collections(collections)

    # Fetch items for a specific collection
    collection_id = collections['collections'][0]['id']
    collection_name = collections['collections'][0]['title']
    print(f"\nFetching items for collection ID: {collection_id}")
    items_metadata = swisstopo.fetch_collection_items(collection_id)

    # Download assets for the collection
    print(f"\nDownloading assets for collection: {collection_name}")
    swisstopo.download_assets(collection_name, items_metadata)

if __name__ == "__main__":
    main()