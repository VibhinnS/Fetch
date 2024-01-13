from scraping_logic.scrape import scrape_amazon_product_details, scrape_unboxify_product_details, scrape_flipkart_product_details
from search_product_url.flipkart_product_url import get_first_flipkart_product_url
from search_product_url.unboxify_product_url import get_first_unboxify_product_url
import csv
import os


def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        product_names = [line.strip() for line in file]
    return product_names


def main():
    flipkart_file_path = 'enter_names/flipkart.txt'
    unboxify_file_path = 'enter_names/unboxify.txt'
    amazon_file_path = 'enter_names/amazon.txt'
    csv_file_path = 'product_details.csv'

    flipkart_product_names = read_names_from_file(flipkart_file_path)
    unboxify_product_names = read_names_from_file(unboxify_file_path)
    amazon_product_urls = read_names_from_file(amazon_file_path)

    all_product_details = []

    for product_name in flipkart_product_names:
        flipkart_url = get_first_flipkart_product_url(product_name)
        if flipkart_url:
            product_details = scrape_flipkart_product_details(flipkart_url, product_name)
            # sleep(10)
            if product_details:
                all_product_details.append(product_details)
            # sleep(10)

    for product_name in unboxify_product_names:
        unboxify_url = get_first_unboxify_product_url(product_name)
        if unboxify_url:
            product_details = scrape_unboxify_product_details(unboxify_url, product_name)
            # sleep(10)
            if product_details:
                all_product_details.append(product_details)

    for amazon_url in amazon_product_urls:
        if amazon_url:
            product_details = scrape_amazon_product_details(amazon_url)
            # sleep(10)
            if product_details:
                all_product_details.append(product_details)
            # sleep(10)

    file_exists = os.path.isfile(csv_file_path)
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Vendor', 'title', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(all_product_details)

    print(f"Results saved to {csv_file_path}")


if __name__ == "__main__":
    main()
