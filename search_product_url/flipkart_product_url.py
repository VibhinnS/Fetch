import requests
from bs4 import BeautifulSoup


def get_first_flipkart_product_url(product_name):
    headers = {
        'User-Agent': 'Your User Agent Here',
    }

    flipkart_url = f"https://www.flipkart.com/search?q={product_name}"
    response = requests.get(flipkart_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first product URL
        first_product_url_element = soup.find('a', {'class': '_1fQZEK'})

        if first_product_url_element:
            first_product_url = first_product_url_element['href']
            return f"https://www.flipkart.com{first_product_url}"
        else:
            print("No product found in Flipkart.")
            return None
    else:
        print(f"Error: {response.status_code} from Flipkart")
        return None
