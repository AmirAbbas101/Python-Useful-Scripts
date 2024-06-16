import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.parse import urljoin, urlparse

def extract_images_from_website(url, folder_path):
    # Create a folder to store images if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    try:
        # Fetch the HTML content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all('img')

        # Extract image URLs and download images
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                # Convert relative URLs to absolute URLs
                img_url = urljoin(url, img_url)
                
                # Remove query parameters, if any
                img_url = img_url.split("?")[0]

                # Extract image file name
                img_name = os.path.basename(urlparse(img_url).path)
                
                # Download image
                img_path = os.path.join(folder_path, img_name)
                urllib.request.urlretrieve(img_url, img_path)
                print(f"Downloaded: {img_url}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch content from {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
website_url = "https://www.uad.edu.pk"
storage_folder = "images"

extract_images_from_website(website_url, storage_folder)
