import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from beautiful_soup import Crawler

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
headers = {"User-agent": user_agent}


class RealEstate:
    def __init__(self, url):
        print(url)
        self.url = url
        self.post_code, self.dataFrame = self.get_data_frame()

    def get_data_frame(self):
        r = requests.get(url=self.url, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        script = soup.find('script', type='application/json')
        if not script:
            return None, None

        contents = script.contents
        if not contents:
            return None, None

        data = json.loads(contents[0])
        if not data:
            return None, None

        if 'query' in data and 'searchParam' in data['query']:
            post_code = data['query']['searchParam']
            # Use post_code as needed
        else:
            return None, None

        if 'props' not in data:
            return None, None
        props = data['props']

        if 'pageProps' not in props:
            return None, None
        pageProps = props['pageProps']

        if '__APOLLO_STATE__' not in pageProps:
            return None, None
        state = pageProps['__APOLLO_STATE__']

        root_query = list(state['ROOT_QUERY'].values())

        totalPages = root_query[1]['totalPages']

        data = {
            "Name": [],
            "Job Title": [],
            "Telephone": [],
            "Mobile": [],
            # "Profile Photo": [],
        }

        df = pd.DataFrame(data)

        for page in range(totalPages):
            page = page + 1
            crawler = Crawler(self.url, page)
            df = df._append(crawler.dataFrame)

        return post_code, df
