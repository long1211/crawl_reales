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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

processed_profiles = set()  # To store processed profiles

# with open(filename, 'w', newline='') as csvfile:
#     fieldnames = ['Name', 'Company', 'Address', 'Phone', 'Website']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for url in urls:
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         profile_urls = []
#         for member in soup.find_all('div', {'class': 'fap-member'}):
#             profile_link = member.find('a', {'href': True}, string='View profile')
#             if profile_link and profile_link['href'] not in processed_profiles:
#                 profile_urls.append(profile_link['href'])
#                 processed_profiles.add(profile_link['href'])
#
#         for profile_url in profile_urls:
#             try:
#                 response = requests.get(profile_url, headers=headers)
#                 profile_soup = BeautifulSoup(response.text, 'html.parser')
#
#                 profile_data = extract_profile_data(profile_soup)
#                 filtered_profile_data = {key: profile_data.get(key, '') for key in fieldnames}
#
#                 writer.writerow(filtered_profile_data)
#                 time.sleep(1)
#             except Exception as e:
#                 print(f"Error fetching {profile_url}: {e}")
