import json
from crawler import RealEstate
from utils.ExcelHelper import write_excel_file

url = 'https://www.domain.com.au/real-estate-agents/darlinghurst-nsw-2010/'
OUTPUT = r'output//'
INPUT = r'sample input//urls.txt'

with open(INPUT, 'r', encoding='utf8') as f:
    urls_dict = json.load(f)

f.close()

for state, urls in urls_dict.items():
    for url in urls:
        realEstate = RealEstate(url)
        dataFrame = realEstate.dataFrame
        if dataFrame is None:
            continue
        elif not dataFrame.empty:
            write_excel_file(OUTPUT + state + '.xlsx', state, dataFrame)
