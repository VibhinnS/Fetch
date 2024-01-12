import requests
from bs4 import BeautifulSoup
from flipkart_product_url import get_first_flipkart_product_url
from unboxify_product_url import get_first_unboxify_product_url
import csv


def scrape_flipkart_product_details(url):
    headers = {
        'User-Agent': 'Your User Agent Here',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('span', {'class': 'B_NuCI'}).get_text(strip=True)
        price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).get_text(strip=True)

        # This selector might need adjustment based on the Amazon page structure
        # description = soup.find('div', {'id': 'productDescription'}).get_text(strip=True)

        return {'title': title, 'price': price}
    else:
        print(f"Error: {response.status_code}")
        return None


def scrape_unboxify_product_details(url):
    headers = {
        'User-Agent': 'Your User Agent Here',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h2', {'class': 'm5'}).get_text(strip=True)
        price = soup.find('h3', {'class': 'f8pr-price s1pr price'}).get_text(strip=True)

        # This selector might need adjustment based on the Amazon page structure
        # description = soup.find('div', {'id': 'productDescription'}).get_text(strip=True)

        return {'title': title, 'price': price}
    else:
        print(f"Error: {response.status_code}")
        return None


def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        product_names = [line.strip() for line in file]
    return product_names


def main():
    flipkart_file_path = 'flipkart.txt'
    unboxify_file_path = 'unboxify.txt'
    csv_file_path = 'product_details.csv'

    flipkart_product_names = read_names_from_file(flipkart_file_path)
    unboxify_product_names = read_names_from_file(unboxify_file_path)

    all_product_details = []

    for product_name in flipkart_product_names:
        flipkart_url = get_first_flipkart_product_url(product_name)
        if flipkart_url:
            product_details = scrape_flipkart_product_details(flipkart_url)
            if product_details:
                all_product_details.append(product_details)

    for product_name in unboxify_product_names:
        unboxify_url = get_first_unboxify_product_url(product_name)
        if unboxify_url:
            product_details = scrape_unboxify_product_details(unboxify_url)
            if product_details:
                all_product_details.append(product_details)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_product_details)

    print(f"Results saved to {csv_file_path}")


if __name__ == "__main__":
    main()
