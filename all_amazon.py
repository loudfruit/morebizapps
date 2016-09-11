# Beautiful Soup searches through html code
# Install with pip install beautifulsoup4
from bs4 import BeautifulSoup
# Another library is required to request html called "requests"
# Install with pip install requests
import requests
import csv

def alookup(search_term):
    url="https://www.amazon.com/s/?field-keywords="
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = url + search_term
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    items = soup.find_all('li','s-result-item')
    csvfile = open('amazing_data.csv', 'a')
    writer = csv.writer(csvfile)
    for item in items:
        name = item.find('h2').text
        price = item.find('span', 's-price').text
        author = item.find('div', 'a-row a-spacing-none').text
        writer.writerow([name, author, price])
    return csv.reader(csvfile)

# for item in items:
#     try:
#         name = item.find('h2').text
#         price = item.find('span', 's-price').text
#         # item_id = item.find('data-asin').text
#         # link =item.find(href=True).['href']
#         writer.writerow([name, price])
#     except:
#         pass
    
