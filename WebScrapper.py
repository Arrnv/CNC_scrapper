from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://dir.indiamart.com/search.mp?ss=cnc+machine+components&v=4&qry_typ=P&current_mcatid=3877&lang=en&wc=3&mcatid=13123&catid=587&src=as-context%7Ckwd%3Dcnc+machine+%7Cpos%3D2%7Ccat%3D587%7Cmcat%3D13123%7Ckwd_len%3D12%7Ckwd_cnt%3D3&qr_nm=gd&res=RC5&com-cf=nl&ptrs=na&ktp=N0&mtp=G&stype=attr%3D1&Mspl=0'
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
})

webpage_1 = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(webpage_1.content, 'html.parser')

links = soup.find_all('a', attrs={'class': 'cardlinks'})
links_list = [link.get('href') for link in links]
l
d = {'Supplier_Name': [], 'Location': [], 'Materials': [],'price': []}

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
        try:
          materials = new_soup.find('td', string='Material').find_next_sibling('td').text.strip()
        except:
          materials = new_soup.find('td', string='material').find_next_sibling('td').text.strip()
      except AttributeError:
          materials = None
      d['Materials'].append(materials)

      try:
          price = new_soup.find('span', attrs={'class': 'bo price-unit'}).text.strip()
      except AttributeError:
          price = None
      d['price'].append(price)
    except:
      print("error")


url = 'https://dir.indiamart.com/search.mp?ss=CNC+Jaws&v=4&qry_typ=P&current_mcatid=3875&lang=en&wc=2&mcatid=13123&catid=587&rdp=pms&qr_nm=gd&res=RC3&com-cf=nl&ptrs=na&ktp=N0&mtp=S&Mspl=0'

webpage_1 = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(webpage_1.content, 'html.parser')

links = soup.find_all('a', attrs={'class': 'cardlinks'})
links_list = [link.get('href') for link in links]
print(len(links_list))
# d = {'Supplier_Name': [], 'Location': [], 'Materials': [],'price': []}

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
        try:
          materials = new_soup.find('td', string='Material').find_next_sibling('td').text.strip()
        except:
          materials = new_soup.find('td', string='material').find_next_sibling('td').text.strip()
      except AttributeError:
          materials = None
      d['Materials'].append(materials)

      # try:
      #     capacity = new_soup.find('td', string='Capacity').find_next_sibling('td').text.strip()
      # except AttributeError:
      #     capacity = None
      # d['Capacity'].append(capacity)

      try:
          price = new_soup.find('span', attrs={'class': 'bo price-unit'}).text.strip()
      except AttributeError:
          price = None
      d['price'].append(price)
    except:
      print("error")



df1 = pd.DataFrame(d)
df1 = df1.dropna(subset=['Supplier_Name'])
df1 = df1.dropna(subset=['price'])
def clean_price(price):
    if pd.isna(price):
        return None
    return int(''.join(filter(str.isdigit, price)))

# Applying the function to the Price column
df1['price'] = df1['price'].apply(clean_price)
df1.to_csv("suplyer.csv")