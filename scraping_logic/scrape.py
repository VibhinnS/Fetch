import requests
from bs4 import BeautifulSoup
from time import sleep


def scrape_flipkart_product_details(url, product_name):
    headers = {
        'User-Agent': 'Your-User-Agent'
    }
    sleep(12)
    response = requests.get(url, headers=headers)
    print("Flipkart Response Accepted")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        sleep(12)
        title = soup.find('span', {'class': 'B_NuCI'}).get_text(strip=True)
        price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).get_text(strip=True)

        # This selector might need adjustment based on the Amazon page structure
        # description = soup.find('div', {'id': 'productDescription'}).get_text(strip=True)
        print("Flipkart product completed successfully")
        return {
            'Vendor': 'Flipkart',
            'title': title,
            'price': price
        }
    else:
        print(f"Error: {response.status_code} from Flipkart scraping {product_name}")
        return None


def scrape_unboxify_product_details(url, product_name):
    headers = {
        'User-Agent': 'Your-User-Agent'
    }
    sleep(12)
    response = requests.get(url, headers=headers)
    print("Unboxify Request Accepted")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        sleep(12)
        title = soup.find('h2', {'class': 'm5'}).get_text(strip=True)
        price = soup.find('h3', {'class': 'f8pr-price s1pr price'}).get_text(strip=True)

        # This selector might need adjustment based on the Amazon page structure
        # description = soup.find('div', {'id': 'productDescription'}).get_text(strip=True)
        print("Unboxify product completed successfully")
        return {
            'Vendor': 'Unboxify',
            'title': title,
            'price': price
        }
    else:
        print(f"Error: {response.status_code} from Unboxify Scraping {product_name}")
        return None


# a different approach has been used for Amazon as it does not allow direct scraping of the website data


def scrape_amazon_product_details(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    sleep(12)
    response = requests.get(url, headers=headers)
    print("Amazon request accepted")

    if response.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in response.text:
            print(f"Page %s was blocked by Amazon. Please try using better proxies\n", url)
        else:
            print(f"Page %s must have been blocked by Amazon as the status code was %d" % (url, response.status_code))
        return None

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        sleep(12)

        title = soup.find('span', {'id': 'productTitle'}).get_text(strip=True)
        price = soup.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
        print("Amazon products added successfully")

        return {
            'Vendor': 'Amazon',
            'title': title,
            'price': price
        }
    except Exception as e:
        print(f"Error while scraping Amazon product details from {url}: {str(e)}")
        return None

