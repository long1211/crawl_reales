import json

import ast
from crawler import RealEstate
from utils.ExcelHelper import write_excel_file

url = 'https://www.domain.com.au/real-estate-agents/darlinghurst-nsw-2010/'
OUTPUT = r'output//'
INPUT = r'sample input//urls.txt'

with open(INPUT, 'r', encoding='utf8') as f:
    urls_dict = json.load(f)

f.close()

count = 0
size = 0

for url in urls_dict.values():
    if size + 10 > count >= size:
        realEstate = RealEstate(url)
        if realEstate.post_code is None:
            continue

        OUTPUT = OUTPUT + realEstate.post_code + '.xlsx'
        write_excel_file(OUTPUT, realEstate.post_code, realEstate.dataFrame)

        # print(url)

    count = count + 1

# url = 'https://www.domain.com.au/real-estate-agents/city-delivery-centre-6000'
# realEstate = RealEstate(url)
# OUTPUT = OUTPUT + realEstate.post_code + '.xlsx'
# write_excel_file(OUTPUT, realEstate.post_code, realEstate.dataFrame)
