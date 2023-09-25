import json
import os

from crawler import RealEstate
from utils.ExcelHelper import write_excel_file

url = 'https://www.domain.com.au/real-estate-agents/darlinghurst-nsw-2010/'
OUTPUT = r'output//'
INPUT = r'sample input//urls.txt'
CRAWLED_URLS = r'sample input//crawled_urls.txt'

with open(INPUT, 'r', encoding='utf8') as f:
    urls_dict = json.load(f)
f.close()

sample_state = 'vic'
crawled_urls = []

for state, urls in urls_dict.items():
    if state != sample_state:
        continue

    if os.path.exists(CRAWLED_URLS):
        with open(CRAWLED_URLS, 'r', encoding='utf8') as f:
            crawled_urls = f.read().split(', ')

    for url in urls:
        if url in crawled_urls:
            continue

        realEstate = RealEstate(url)
        f = open(CRAWLED_URLS, "a")
        f.write(url + ', ')
        f.close()
        dataFrame = realEstate.dataFrame

        if dataFrame is None:
            continue
        elif not dataFrame.empty:
            write_excel_file(OUTPUT + state + '.xlsx', state, dataFrame)
