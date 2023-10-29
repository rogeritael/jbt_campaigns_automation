from controllers.BingController import BingController
from controllers.LinkedInController import LinkedInController

class Processors:
    def __init__(self):
        self.teste = ''

    def run_bing(self, sheets, file_path: str):
        prev_month = int(file_path.split('_')[1].replace('.csv','')) -1
        
        # se o nome arquivo estiver com apenas 9 sem o 0 na frente, adicionamos hardcoded 
        current_month = prev_month + 1
        if(current_month < 10):
            file_path = f'{file_path.split('_')[0]}_0{int(file_path.split('_')[1].replace('.csv', ''))}.csv'

        if(prev_month < 10):
            prev_month = f'0{int(file_path.split('_')[1].replace('.csv','')) -1}'

        prev_path = f'{file_path.split('_')[0]}_{prev_month}.csv' 

        # classes dos controladores
        bingManager = BingController()
        # sheets = SheetController()

        # recuperando as campanhas de cada arquivos
        current_campaigns = bingManager.findCampaigns(file_path)
        prev_campaigns = bingManager.findCampaigns(prev_path)

        # criaçao do pagina e header da midia
        bing_page = sheets.createSheet('Bing')

        with open(file_path, 'r') as file:
            campaigns = bingManager.findCampaigns(file)

        with open(prev_path, 'r') as file:
            prev_campaigns = bingManager.findCampaigns(file)

        current = []
        headers = [1,2]

        sheets.createHeader('Bing Ads', 5, 20)

        # pega cada header com nome de campanha e salva em headers para ser feito a estilizaçao
        for header in range(len(campaigns) - 1):
            rows_per_campaign = 6
            headers.append(headers[-1] + rows_per_campaign)

        for index, campaign in campaigns.iterrows():
            campaign = bingManager.processCampaign(campaign, file_path)
            current = campaign

            sheets.createHeader(campaign['name'], 5)
            sheets.createRow(['Mes','Investimento','Impressoes','Cliques','CPC','CTR'], highlight=True)
            sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR']])

            for index, campaign in prev_campaigns.iterrows():
                campaign = bingManager.processCampaign(campaign, prev_path)
                if(campaign['name'] == current['name']):
                    sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR']])
                    sheets.createRow([
                        'Variaçao',
                        f'{(current['investiment']/campaign['investiment'] -1):.2f}%',
                        f'{(current['impressions']/campaign['impressions'] -1):.2f}%',
                        f'{(current['clicks']/campaign['clicks'] -1):.2f}%',
                        f'{(current['CPC'] /campaign['CPC'] -1):.2f}%',
                        f'{(float(str(current['CTR']).replace('%',''))/float(str(campaign['CTR']).replace('%','')) -1):.2f}%'
                    ],
                        highlight=True
                    )
                    sheets.createRow([''])

    def run_linkedin(self, sheets, file_path: str):
        prev_month = int(file_path.split('_')[1].replace('.csv','')) -1
        
        current_month = prev_month + 1
        if(current_month < 10):
            file_path = f'{file_path.split('_')[0]}_0{int(file_path.split('_')[1].replace('.csv', ''))}.csv'

        if(prev_month < 10):
            prev_month = f'0{int(file_path.split('_')[1].replace('.csv','')) -1}'

        prev_path = f'{file_path.split('_')[0]}_{prev_month}.csv' 
        lkdManager = LinkedInController()

        # current_campaigns = lkdManager.findCampaigns(file_path)
        prev_campaigns = lkdManager.findCampaigns(prev_path)

        # print(current_campaigns)