import pandas as pd


class RealEstate:
    def __init__(self, data):
        self.data = data
        self.agents = self.get_agents()
        self.dataFrame = self.getDataFrame()

    def get_agents(self):
        SalesPeople = list(self.data.values())[6]
        agents = SalesPeople['agents']

        id_list = []
        for agent in agents:
            id_list.append(agent['id'])

        return id_list

    def getDataFrame(self):
        url = []
        name = []
        totalReviews = []
        avgRating = []
        jobTitle = []
        primaryListCount = []
        secondaryListCount = []
        phone = []
        agency = []

        for agent in self.agents:
            url.append(self.data[agent]['url'])
            name.append(self.data[agent]['name'])
            totalReviews.append(self.data[agent]['totalReviews'])
            avgRating.append(self.data[agent]['avgRating'])
            jobTitle.append(self.data[agent]['jobTitle'])
            primaryListCount.append(self.data[agent]['primaryListCount'])
            secondaryListCount.append(self.data[agent]['primaryListCount'])

            phone_id = self.data[agent]['phone']['id']
            phone_mobile = self.data[phone_id]['mobile']
            phone.append(phone_mobile)

            agency_id = self.data[agent]['agency']['id']
            agency_name = self.data[agency_id]['name']
            agency.append(agency_name)

        data = {
            "url": url,
            "Name": name,
            "Total Reviews": totalReviews,
            "Rating": avgRating,
            "Job Title": jobTitle,
            "Primary List Count": primaryListCount,
            "Secondary List Count": secondaryListCount,
            "Phone": phone,
            "Agency": agency,
        }

        df = pd.DataFrame(data)

        return df
