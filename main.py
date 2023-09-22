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
size = 1010

for url in urls_dict.values():
    count = count + 1
    if size + 10 > count >= size:
        realEstate = RealEstate(url.lower())
        if realEstate.post_code is None:
            continue

        write_excel_file(OUTPUT + realEstate.post_code + '.xlsx', realEstate.post_code, realEstate.dataFrame)

    elif size + 10 <= count:
        break

# url = 'https://www.domain.com.au/real-estate-agents/city-delivery-centre-6000'
# realEstate = RealEstate(url)
# OUTPUT = OUTPUT + realEstate.post_code + '.xlsx'
# write_excel_file(OUTPUT, realEstate.post_code, realEstate.dataFrame)
