import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
cookie = 'reauid=06f1281717711a00f009ee645e020000f2510000; split_audience=e; _gcl_au=1.1.1907106518.1693321722; s_ecid=MCMID%7C88716507636484320892649920831798867709; mid=96586206457448367; _gid=GA1.3.1641794989.1693617218; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%224d2fbc30-e9a3-0b15-5b00-abffb46e720d%22%2C%22c%22%3A1693617646674%2C%22l%22%3A1693617646674%7D; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%222171b0a4-9ead-24ee-7b65-a9892e267d97%22%2C%22e%22%3A1693619446682%2C%22c%22%3A1693617646668%2C%22l%22%3A1693617646682%7D; fullstory_audience_split=B; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; s_cc=true; DM_SitId1464=1; DM_SitId1464SecId12708=1; Country=LA; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2Ffind-agent%2F3002%3Ftimeframe%3D-24~1693888871402%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fagent%2Fliam-carrington-1803302%3FcampaignType%3Dinternal%26campaignChannel%3Din_product%26campaignSource%3Drea%26campaignName%3Dsell_enq%26campaignPlacement%3Dagent_search_result_card%26campaignKeyword%3Dagency_marketplace%26sourcePage%3Dagent_srp%26sourceElement%3Dagent_search_result_card~1693907839554; VT_LANG=language%3Den-US; s_sq=%5B%5BB%5D%5D; KP_UIDz-ssn=03W53CCaVbgYjpqappMENxbigODBnyR69FDcOrULk3oUwdxlN1N7BOuBBYKhOvaccLfxyTFr6r5mdSHLUkEUshTMcZNUMC4mDtkuyqcEUxdcWYuAPOcinncdIuRmricBGEvUC2UI7C6ZRVrEtX6jjeo4Xo09V29; KP_UIDz=03W53CCaVbgYjpqappMENxbigODBnyR69FDcOrULk3oUwdxlN1N7BOuBBYKhOvaccLfxyTFr6r5mdSHLUkEUshTMcZNUMC4mDtkuyqcEUxdcWYuAPOcinncdIuRmricBGEvUC2UI7C6ZRVrEtX6jjeo4Xo09V29; KP2_UIDz-ssn=0Nusxzt9NwMZOm3mDBq56zLgewUoAgpumnBZ8BBUa5GyMCMSWNyqkSD8wSPkzpzK7wuRIBxzmJMgkaYQKLx7fs3ojizlLmMarRMXI512gGFolcOZM7PjUCFUXRwdFetKvylWNkeKUOqH7zwumNVWogsKVpcz8; KP2_UIDz=0Nusxzt9NwMZOm3mDBq56zLgewUoAgpumnBZ8BBUa5GyMCMSWNyqkSD8wSPkzpzK7wuRIBxzmJMgkaYQKLx7fs3ojizlLmMarRMXI512gGFolcOZM7PjUCFUXRwdFetKvylWNkeKUOqH7zwumNVWogsKVpcz8; pageview_counter.srs=16; s_nr30=1693960448750-Repeat; myid5_id=ID5*BJl2NeGvRZsbxPHXQtbITS2O_rdi9j_YZ9pCj06kg-RfhyfmLq8cf6jESV0eTFCoX4hvuwmji1XfyR6Jf9v4jg; _sp_ses.2fe7=*; _sp_id.2fe7=d4118ea6-7d67-41a9-b20a-2446e2eeb378.1693321722.18.1693960449.1693934525.2be85c68-04ed-451b-9c6d-471a8697cdc5; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19607%7CMCMID%7C88716507636484320892649920831798867709%7CMCAAMLH-1694565249%7C3%7CMCAAMB-1694565249%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1693967649s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; _gat_gtag_UA_143679184_2=1; utag_main=v_id:018a41d6e658004396cfc05d91800506f001e067007e8$_sn:18$_se:1$_ss:1$_st:1693962247485$vapi_domain:realestate.com.au$dc_visit:18$ses_id:1693960447485%3Bexp-session$_pn:1%3Bexp-session$_prevpage:rea%3Afind%20agent%3Aagent%3Asearch%20results%3Bexp-1693964048746$dc_event:1%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _ga_F962Q8PWJ0=GS1.1.1693960446.17.1.1693960450.0.0.0; _ga=GA1.1.1229579892.1693321722; _ga_3J0XCBB972=GS1.1.1693960446.19.1.1693960450.0.0.0; _lr_geo_location_state=VT; _lr_geo_location=LA; nol_fpid=lybflbwyz7ujm4jysxsom1bjbexsz1693321722|1693321722111|1693960449876|1693960451312'


class Crawler:
    def __init__(self, url, page):
        self.page = page

        self.URL = url + '?page=' + str(page)
        self.headers = {
            'User-agent': user_agent,
            # 'Cookie': cookie,
        }

        self.dataFrame = self.crawl()

    def crawl(self):
        r = requests.get(url=self.URL, headers=self.headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        data = json.loads(soup.find('script', type='application/json').contents[0])
        if not data:
            return self.getDataFrame([])

        if 'props' not in data:
            return self.getDataFrame([])
        props = data['props']

        if 'pageProps' not in props:
            return self.getDataFrame([])
        pageProps = props['pageProps']

        if '__APOLLO_STATE__' not in pageProps:
            return self.getDataFrame([])
        state = pageProps['__APOLLO_STATE__']

        data = []

        for key in state:
            if key.__contains__('ContactSearchContact:'):
                data.append(state[key])

        return self.getDataFrame(data)

    @staticmethod
    def getDataFrame(data):
        name = []
        jobTitle = []
        telephone = []
        mobile = []
        # profilePhoto = []

        for agent in data:
            name.append(agent['name'])
            jobTitle.append(agent['jobTitle'])
            telephone.append(agent['telephone'])
            mobile.append(agent['mobile'])
            # profilePhoto.append(agent['profilePhoto'])

        data = {
            "Name": name,
            "Job Title": jobTitle,
            "Telephone": telephone,
            "Mobile": mobile,
            # "Profile Photo": profilePhoto,
        }

        df = pd.DataFrame(data)

        return df
