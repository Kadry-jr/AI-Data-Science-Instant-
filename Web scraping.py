# web scraping for data to a website that sells home accesories prouducts with BeautifulSoup library and saving it in a csv file

import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the website
secret_input = input()
base_url = f'https://the{secretInput}egypt.com/collections/home-accesories-1'

# List to store all products
all_products = []

# Iterate through pages
for page_number in range(1, 22):
    # Construct the URL for the current page
    url = f'{base_url}?page={page_number}'

    # Send a GET request to the URL
    page = requests.get(url)
    if page.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(page.content, 'html.parser')
        products = soup.find("div", {'class' : 'tt-product-listing'})

        # Extract product details
        for product in products.find_all("div", {'class' : 'tt-product'}):
            product_name = product.find('h2').text.strip()
            product_price = product.find("div", {'class' : 'tt-price'}).text.strip()
            product_vendor = product.find('li').text.strip()
            product_status = product.find("span", {'class' : 'tt-label-our-stock'}).text.strip() if product.find("span", {'class' : 'tt-label-our-stock'}) else 'Available'
            # Append product details to the list
            all_products.append({
                "Product Name": product_name,
                "Product Price": product_price,
                "Product Vendor": product_vendor,
                "Product Status": product_status
            })

    else:
        print(f"Failed to retrieve web page {url}. Status code: {page.status_code}")

# Save the scraped data to a CSV file
file_path = 'C:\\Users\\Abd El-Rahman\\Desktop\\webscrabing\\data.csv'
with open(file_path, 'w', newline='') as final_file:
    dict_writer = csv.DictWriter(final_file, fieldnames=all_products[0].keys())

    # Write the header row
    dict_writer.writeheader()

    # Write each product to the CSV file
    for product in all_products:
        dict_writer.writerow(product)

    print("CSV file saved successfully!")

