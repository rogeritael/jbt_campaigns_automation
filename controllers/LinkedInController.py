import pandas as pd
import os
import re

class LinkedInController:
    def __init__(self):
        self.months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro' ,'Dezembro']

    def findCampaigns(self, file) -> []:
            csv_file = pd.read_csv(file, sep="\t", encoding='utf-16')
            campaigns = csv_file[csv_file['Nome da campanha'] != '-']
            
            return campaigns
    
    def processCampaign(self, campaign, file_path):
        file_name = os.path.basename(file_path)
        month = int(file_name.split('.csv')[0].split('linkedin_')[1])

        campaign = {
            'name': campaign['Nome do grupo de campanhas'],
            'investiment': campaign['Total investido'],
            'impressions': campaign['Impressões'],
            'clicks': campaign['Cliques'],
            'CTR': (int(campaign['Cliques'])/int(campaign['Impressões'])),
            'CPC': (float(campaign['Total investido'].replace(',','.'))/float(campaign['Cliques'])),
            'leads': campaign['Leads'],
            'month': self.months[month - 1],
        }

        return campaign