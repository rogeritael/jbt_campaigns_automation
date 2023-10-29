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