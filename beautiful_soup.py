import requests
from bs4 import BeautifulSoup
import json

from utils.ExcelHelper import write_excel_file
from utils.filter_sale_data import RealEstate

OUTPUT = r'output//real-estate.xlsx'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
cookie = 'reauid=06f1281717711a00f009ee645e020000f2510000; split_audience=e; _gcl_au=1.1.1907106518.1693321722; s_ecid=MCMID%7C88716507636484320892649920831798867709; VT_LANG=language%3Dvi; mid=96586206457448367; _gid=GA1.3.1641794989.1693617218; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%224d2fbc30-e9a3-0b15-5b00-abffb46e720d%22%2C%22c%22%3A1693617646674%2C%22l%22%3A1693617646674%7D; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%222171b0a4-9ead-24ee-7b65-a9892e267d97%22%2C%22e%22%3A1693619446682%2C%22c%22%3A1693617646668%2C%22l%22%3A1693617646682%7D; fullstory_audience_split=B; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; s_cc=true; DM_SitId1464=1; DM_SitId1464SecId12708=1; Country=LA; myid5_id=ID5*NMQ_btHyDMArmbiMcouBFh3Tt-xSq3aDV4cL1H75yr9fVZiwZl0tW74q0YhAjDW5X1b5U_3GIfwLewP04qRLlw; s_sq=%5B%5BB%5D%5D; _lr_geo_location_state=VT; _lr_geo_location=LA; KP_UIDz-ssn=037Ct3aKcVzBbfLgVZVrmh2VsbsAYW9AdnI6sbKAs4oeP8D98jZ0l0ds2quo1DIVOODBhIX7ZcgCy3ZLuYMORJPd1edKZ8NXc9wdZZIR1IR67QjU4TjiCdH55UuvbD5CEJJ3itsdQObQVkECIddKrBQD4H5unPy; KP_UIDz=037Ct3aKcVzBbfLgVZVrmh2VsbsAYW9AdnI6sbKAs4oeP8D98jZ0l0ds2quo1DIVOODBhIX7ZcgCy3ZLuYMORJPd1edKZ8NXc9wdZZIR1IR67QjU4TjiCdH55UuvbD5CEJJ3itsdQObQVkECIddKrBQD4H5unPy; KP2_UIDz-ssn=0RMwHp0aNvMpu9RIAOLswApu2KY8dXmwIch5Q8Gb4vYxyKm4q4CVAhl5bxzQ592IuE34xhaJfuOyR3FOxavo6A73jN3jhqchmuSGN2be51GdE27iHnITyoVL4NAKgGPi0wKOLvd2861CNbsPjJ7SD5ZVTcZwe; KP2_UIDz=0RMwHp0aNvMpu9RIAOLswApu2KY8dXmwIch5Q8Gb4vYxyKm4q4CVAhl5bxzQ592IuE34xhaJfuOyR3FOxavo6A73jN3jhqchmuSGN2be51GdE27iHnITyoVL4NAKgGPi0wKOLvd2861CNbsPjJ7SD5ZVTcZwe; pageview_counter.srs=12; s_nr30=1693882374522-Repeat; _sp_ses.2fe7=*; _sp_id.2fe7=d4118ea6-7d67-41a9-b20a-2446e2eeb378.1693321722.13.1693882375.1693870904.22eb2746-e940-4e18-a4e2-e6b53ec955cb; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19605%7CMCMID%7C88716507636484320892649920831798867709%7CMCAAMLH-1694487174%7C3%7CMCAAMB-1694487174%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1693889574s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; _gat_gtag_UA_143679184_2=1; utag_main=v_id:018a41d6e658004396cfc05d91800506f001e067007e8$_sn:13$_se:1$_ss:1$_st:1693884173757$vapi_domain:realestate.com.au$dc_visit:13$ses_id:1693882373757%3Bexp-session$_pn:1%3Bexp-session$_prevpage:rea%3Afind%20agent%3Aagent%3Asearch%20results%3Bexp-1693885974521$dc_event:1%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _ga_3J0XCBB972=GS1.1.1693882038.14.1.1693882375.0.0.0; _ga=GA1.1.1229579892.1693321722; _ga_F962Q8PWJ0=GS1.1.1693882038.12.1.1693882375.0.0.0; nol_fpid=lybflbwyz7ujm4jysxsom1bjbexsz1693321722|1693321722111|1693882375472|1693882376086; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2Fagent%2Fliam-carrington-1803302%3FcampaignType%3Dinternal%26campaignChannel%3Din_product%26campaignSource%3Drea%26campaignName%3Dsell_enq%26campaignPlacement%3Dagent_search_result_card%26campaignKeyword%3Dagency_marketplace%26sourcePage%3Dagent_srp%26sourceElement%3Dagent_search_result_card~1693870908520%7Chttps%3A%2F%2Fwww.realestate.com.au%2Ffind-agent%2F3002%3Ftimeframe%3D-24~1693882378777'


class Crawler:
    def __init__(self, postcode):
        self.postcode = postcode

        self.URL = 'https://www.realestate.com.au/find-agent/' + str(postcode)
        self.headers = {
            'User-agent': user_agent,
            'Cookie': cookie,
        }

        self.crawl()

    def crawl(self):
        r = requests.get(url=self.URL, headers=self.headers)
        # If this line causes an error, run 'pip install html5lib' or install html5lib
        soup = BeautifulSoup(r.content, 'html5lib')

        for sc in soup.findAll('script'):
            sc_str = str(sc.string)

            if sc_str.__contains__('window.__APOLLO_STATE__'):
                app_config = sc_str.split('window.__APP_CONFIG__=')[0]
                apollo_state = app_config.split('window.__APOLLO_STATE__=')[1]
                apollo_state = apollo_state.split('}};')[0]
                apollo_state = apollo_state + '}}'

                apollo_state_dict = json.loads(apollo_state)

                real_estate = RealEstate(apollo_state_dict)

                dataFrame = real_estate.dataFrame
                # print(dataFrame)

                write_excel_file(OUTPUT, self.postcode, dataFrame)
