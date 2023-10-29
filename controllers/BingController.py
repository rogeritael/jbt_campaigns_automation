import pandas as pd
import os

class BingController:
    def __init__(self):
        self.months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro' ,'Dezembro']

    def findCampaigns(self, file) -> []:
        csv_file = pd.read_csv(file, sep=",")

        campaigns = csv_file[csv_file['Campaign'] != '-']

        return campaigns

    def processCampaign(self, campaign, file_path):
        file_name = os.path.basename(file_path)
        month = int(file_name.split('.csv')[0].split('bing_')[1])

        campaign = {
            'name': campaign['Campaign'].encode('latin1').decode('utf-8'),
            'impressions': campaign['Impr.'],
            'investiment': campaign['Spend'],
            'clicks': campaign['Clicks'],
            'CPC': campaign['Avg. CPC'],
            'CTR': campaign['CTR'],
            'month': self.months[month - 1],
        }

        return campaign