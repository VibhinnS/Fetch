import requests
from bs4 import BeautifulSoup
from time import sleep


def get_first_unboxify_product_url(product_name):
    headers = {
        'User-Agent': 'Your User Agent Here',
    }

    unboxify_url = f"https://www.unboxify.in/search?q={product_name}"
    response = requests.get(unboxify_url, headers=headers)
    sleep(12)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        sleep(12)
        # Find the first figure tag
        first_figure_tag = soup.find('figure')

        if first_figure_tag:
            # Find the first anchor tag within the figure tag
            first_product_url_element = first_figure_tag.find('a')

            if first_product_url_element:
                first_product_url = first_product_url_element['href']
                return f"https://www.unboxify.in{first_product_url}"

        print("No product found on Unboxify.")
        return None

    else:
        print(f"Error: {response.status_code} from Unboxify")
        return None
