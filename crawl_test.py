import csv
import requests
from bs4 import BeautifulSoup
import time
import yaml


def extract_profile_data(profile_soup):
    table = profile_soup.find('table')
    data = {}
    for row in table.find_all('tr', {'class': 'Divider'}):
        label_td, value_td = row.find_all('td')
        label = label_td.get_text().strip()
        value = value_td.get_text().strip()
        data[label] = value
    return data


def get_csv_data():
    csv_url = "https://github.com/schappim/australian-postcodes/raw/master/australian-postcodes.csv"
    response = requests.get(csv_url)
    decoded_content = response.content.decode('utf-8')
    cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    return list(cr)


def get_urls_from_config(csv_data):
    urls = []
    with open("sample input/config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
        for row in csv_data:
            formatted_suburb = row['Suburb'].replace(' ', '-').lower()
            if config['type'] == 'postcode' and row['Postcode'] == str(config['value']):
                urls.append(f"https://www.domain.com.au/real-estate-agencies/{formatted_suburb}-{row['Postcode']}")
            elif config['type'] == 'state' and row['State'] == config['value']:
                urls.append(f"https://www.domain.com.au/real-estate-agencies/{formatted_suburb}-{row['Postcode']}")
            elif config['type'] == 'country':
                urls.append(f"https://www.domain.com.au/real-estate-agencies/{formatted_suburb}-{row['Postcode']}")
    return urls


def get_csv_filename_from_config():
    with open("sample input/config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
        return f"profile_data_{config['type']}_{config['value']}.csv"


csv_data = get_csv_data()
urls = get_urls_from_config(csv_data)
filename = get_csv_filename_from_config()

print(urls)

