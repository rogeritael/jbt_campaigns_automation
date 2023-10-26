import locale

from controllers.SheetController import SheetController
from controllers.BingController import BingController
locale.setlocale(locale.LC_ALL, 'pt-BR-UTF-8')

file_path = './csv/bing_09.csv'

bingManager = BingController()

sheets = SheetController()
bing_page = sheets.createSheet('bing')

current_campaign = ''
# with open(file_path, 'r') as file:

campaigns = bingManager.findCampaigns(file_path)

sheets.createRow(['Bing Ads'])

for index, campaign in campaigns.iterrows():
    campaign = bingManager.processCampaign(campaign, file_path)
    sheets.createRow([campaign['name']])
    sheets.createRow(['Mes','Investimento','Impressoes','Cliques','CPC','CTR'])
    sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR']])
    sheets.createRow([''])

    sheets.setHeader('A1','F1')
    sheets.setHeader('A2','F2')



        # sheets.createSubHeader([campaign['name']], 'ffffff')
        
        # sheets.createSubHeader(['Mes', 'Investimento', 'Impressoes', 'Cliques', 'CPC', 'CTR'], 'ffffff')
        # sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR']])

        # # pega o arquivo do mes anterior
        # prev_month = int(file_path.split('_')[1].split('.csv')[0]) -1

        # if(prev_month < 10):
        #     prev_month = f'0{prev_month}'

        # prev_path = f'{file_path.split('_')[0]}_{prev_month}.csv'

        # current_campaign = campaign

        # with open(prev_path, 'r') as prev_campaigns:
        #     prev_campaigns = bingManager.findCampaigns(prev_campaigns)
            
        #     for index, campaign in prev_campaigns.iterrows():
        #         if(campaign['Campaign'].encode('latin1').decode('utf-8') == current_campaign['name']):
        #             campaign = bingManager.processCampaign(campaign, prev_path)
        #             sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR']])
        #             sheets.createRow([
        #                 'Variaçao',
        #                 f'{(current_campaign['investiment']/campaign['investiment'] -1):.2f}%',
        #                 f'{(current_campaign['impressions']/campaign['impressions'] -1):.2f}%',
        #                 f'{(current_campaign['clicks']/campaign['clicks'] -1):.2f}%',
        #                 f'{(current_campaign['CPC'] /campaign['CPC'] -1):.2f}%',
        #                 f'{(float(str(current_campaign['CTR']).replace('%',''))/float(str(campaign['CTR']).replace('%','')) -1):.2f}%'
        #                 # f'{(float(current_campaign["CTR"].replace("%", "")) / float(campaign["CTR"].replace("%", "")) - 1):.2f}%
        #             ])
        #             sheets.createRow([''])

sheets.save()