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

for url in urls_dict.values():
    print(url)

# url = 'https://www.domain.com.au/real-estate-agents/city-delivery-centre-6000'
# realEstate = RealEstate(url)
# OUTPUT = OUTPUT + realEstate.post_code + '.xlsx'
# write_excel_file(OUTPUT, realEstate.post_code, realEstate.dataFrame)
