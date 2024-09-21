# Swisstopo Data Access

This project provides tools to access and download geospatial data from the Swisstopo API. The main functionalities include browsing available collections, fetching items from specific collections, and downloading associated assets.

## Project Structure
. ├── access_swisstopo.py ├── README.md ├── execute.py

# Swisstopo Datenzugriff

Dieses Projekt bietet Werkzeuge zum Zugriff auf und Herunterladen von Geodaten aus der Swisstopo API. Die Hauptfunktionen umfassen das Durchsuchen verfügbarer Sammlungen, das Abrufen von Elementen aus bestimmten Sammlungen und das Herunterladen zugehöriger Assets.

## Projektstruktur
. ├── access_swisstopo.py ├── README.md ├── execute.py


## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Initialize the SwisstopoAccess class and fetch collections:**
    ```python
    from access_swisstopo import SwisstopoAccess

    swisstopo = SwisstopoAccess()
    collections = swisstopo.get_collections()
    swisstopo.browse_collections(collections)
    ```

2. **Fetch items for a specific collection and download assets:**
    ```python
    collection_id = collections['collections'][0]['id']
    collection_name = collections['collections'][0]['title']
    items_metadata = swisstopo.fetch_collection_items(collection_id)
    swisstopo.download_assets(collection_name, items_metadata)
    ```

3. **Run the example script:**
    ```sh
    python execute.py
    ```

## License

This project is licensed under the MIT License.

---

