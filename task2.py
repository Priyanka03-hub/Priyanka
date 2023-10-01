import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bbc.com/news'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('div', class_='gs-c-promo')

    data = []

    for article in articles:
        title = article.find('h3').text.strip()
        link = article.find('a')['href']
        data.append([title, link])

    csv_filename = 'bbc_news_data.csv'

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['Title', 'Link'])

        csv_writer.writerows(data)

    print(f'Data has been successfully scraped and saved to {csv_filename}.')
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
