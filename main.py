import json

import pandas as pd
import requests
from bs4 import BeautifulSoup

from beautiful_soup_2 import Crawler2
from utils.ExcelHelper import write_excel_file

url = 'https://www.domain.com.au/real-estate-agents/darlinghurst-nsw-2010/'

OUTPUT = r'output//'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
headers = {"User-agent": user_agent}

r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
data = json.loads(soup.find('script', type='application/json').contents[0])

post_data = data['query']['searchParam']
OUTPUT = OUTPUT + post_data + '.xlsx'

state = data['props']['pageProps']['__APOLLO_STATE__']
root_query = list(state['ROOT_QUERY'].values())

totalPages = root_query[1]['totalPages']

data = {
    "Name": [],
    "Job Title": [],
    "Telephone": [],
    "Mobile": [],
    "Profile Photo": [],
}

df = pd.DataFrame(data)

for page in range(totalPages):
    page = page + 1
    crawler = Crawler2(url, page)
    df = df._append(crawler.dataFrame)

write_excel_file(OUTPUT, post_data, df)
