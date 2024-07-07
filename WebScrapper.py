from bs4 import BeautifulSoup
import requests
import pandas as pd

# List of URLs to scrape
urls = [
    'https://dir.indiamart.com/search.mp?ss=cnc+machine+components&v=4&qry_typ=P&current_mcatid=3877&lang=en&wc=3&mcatid=13123&catid=587&src=as-context%7Ckwd%3Dcnc+machine+%7Cpos%3D2%7Ccat%3D587%7Cmcat%3D13123%7Ckwd_len%3D12%7Ckwd_cnt%3D3&qr_nm=gd&res=RC5&com-cf=nl&ptrs=na&ktp=N0&mtp=G&stype=attr%3D1&Mspl=0',
    'https://dir.indiamart.com/search.mp?ss=CNC+Jaws&v=4&qry_typ=P&current_mcatid=3875&lang=en&wc=2&mcatid=13123&catid=587&rdp=pms&qr_nm=gd&res=RC3&com-cf=nl&ptrs=na&ktp=N0&mtp=S&Mspl=0'
]

# Define headers for the requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Dictionary to store the scraped data
d = {'Supplier_Name': [], 'Location': [], 'Materials': [], 'price': []}

def clean_price(price):
    if pd.isna(price):
        return None
    return int(''.join(filter(str.isdigit, price)))

# Loop through each URL to scrape data
for url in urls:
    try:
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        # Find all the links to the product cards
        links = soup.find_all('a', attrs={'class': 'cardlinks'})
        links_list = [link.get('href') for link in links]

        # Iterate through each link to collect data
        for link in links_list:
            try:
                new_page = requests.get(link, headers=HEADERS)
                new_soup = BeautifulSoup(new_page.content, 'html.parser')

                try:
                    supplier_name = new_soup.find('h2', attrs={'class': "fs15 bo"}).text.strip()
                except AttributeError:
                    supplier_name = None
                d['Supplier_Name'].append(supplier_name)

                try:
                    location = new_soup.find('div', attrs={'class': 'fs12 color1 dsf addrs plhn'}).text.strip()
                except AttributeError:
                    location = None
                d['Location'].append(location)

                try:
                    materials = new_soup.find('td', string='Material').find_next_sibling('td').text.strip()
                except AttributeError:
                    materials = None
                d['Materials'].append(materials)

                try:
                    price = new_soup.find('span', attrs={'class': 'bo price-unit'}).text.strip()
                except AttributeError:
                    price = None
                d['price'].append(price)
            except Exception as e:
                print(f"Error processing link {link}: {e}")

    except Exception as e:
        print(f"Error accessing URL {url}: {e}")

# Convert the dictionary to a DataFrame
df1 = pd.DataFrame(d)

# Clean the DataFrame
df1 = df1.dropna(subset=['Supplier_Name'])
df1 = df1.dropna(subset=['price'])
df1['price'] = df1['price'].apply(clean_price)

# Export the DataFrame to a CSV file
df1.to_csv("suplyer.csv", index=False)

print("Data collection complete. CSV file created.")
