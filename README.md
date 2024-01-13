# Fetch E-Com Store Prices Automated Pipeline

A tool to fetch prices across Flipkart, Amazon and Unboxify for different products and track them.

Project structure - 

1. Add your desired products in `enter_names` directory. Add Flipkart products in `flipkart.txt`, and Unboxify products in `unboxify.txt`
2. Amazon scraping works via directly pasting product URLs in `amazon.txt` file.
3. Scraping logic is written in a single file `scrape.py`
4. URL fetching is done via `search_product_url` directory.

## Usage

From a terminal 

1. Clone this project  `git clone https://github.com/VibhinnS/price_fetching_automation.git` and cd into it `cd price_fetching_automation`
2. Add a Virtual Environment `python3 -m venv .venv` (Optional)
3. Activate the Virtual Environment `source .venv/bin/activate` (Optional) 
4. Install Requirements `pip3 install -r requirements.txt`
5. Rum python3 `main.py`

## Example Output - 'product_details.csv'
### Product Details
```csv
Flipkart,"realme Narzo 50 Pro 5G (Hyper Black, 128 GB)(8 GB RAM)","₹27,999"
Unboxify,"Samsung Galaxy Buds Pro | 99% Noise Cancellation, Wireless Charging, 28 Hrs Playtime (UNBOXED) 🥇","Rs. 5,990.00 Incl. GSTRs. 17,990.00"
Unboxify,Apple AirPods Pro (UNBOXED) 🥇,"Rs. 12,900.00 Incl. GSTRs. 24,900.00"
Amazon,"JUTERI Plastic Studio 6 XL Free Standing Chest of Drawers (30 Cm X 38 Cm X 116 Cm) Standard (Multicolour, 6XL Multi Big Size(6XL), Matte)",999.
Amazon,"Samsung Galaxy F34 5G (Orchid Violet, 6 GB RAM, 128 GB Storage) | 50 MP No Shake Camera | Auto Night Mode | 120 Hz AMOLED Display | 4K Videos | 6000 mAh Large Battery | Dolby Atmos | Gorilla Glass 5","18,999."
```

### Input Example 
flipkart.txt - 

```text
Realme Narzo 50 Pro
Motorola Edge 40
```


unboxify.txt - 
```text
Samsung Buds 2
Apple AirPods
```


amazon.txt (add product URLs directly) - 
```text
https://www.amazon.in/JUTERI-Plastic-Standing-Standard-Multicolour/dp/B0BNLGQZJQ/ref=cm_cr_arp_d_product_top?ie=UTF8
https://www.amazon.in/Samsung-Storage-Display-Battery-Gorilla/dp/B0CL5J9X7N/ref=sr_1_1?crid=14B7J8F3001E9&keywords=samsung+f34&qid=1705147276&s=electronics&sprefix=samsung+f3%2Celectronics%2C204&sr=1-1
```
