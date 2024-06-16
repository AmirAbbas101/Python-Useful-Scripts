import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.parse import urljoin, urlparse

def extract_images_from_page(url, folder_path, visited_urls):
    # Add the URL to visited_urls to avoid visiting the same page again
    visited_urls.add(url)

    try:
        # Fetch the HTML content of the page
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

        # Find all links on the page
        links = soup.find_all('a', href=True)
        
        # Extract and process all linked pages recursively
        for link in links:
            next_url = urljoin(url, link['href'])
            if next_url not in visited_urls:
                extract_images_from_page(next_url, folder_path, visited_urls)

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch content from {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to crawl the entire website and download images
def crawl_website(url, storage_folder):
    visited_urls = set()
    extract_images_from_page(url, storage_folder, visited_urls)


# Example usage:
website_url = input("Enter URL: ")
storage_folder = "images"

crawl_website(website_url, storage_folder)
