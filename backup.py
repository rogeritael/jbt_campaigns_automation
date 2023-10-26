# controllers
from controllers.SheetController import SheetController
from controllers.BingController import BingController

# diretorio dos arquivos
file_path = './csv/bing_09.csv'

prev_month = int(file_path.split('_')[1].replace('.csv','')) -1
if(prev_month < 10):
    prev_month = f'0{int(file_path.split('_')[1].replace('.csv','')) -1}'

prev_path = f'{file_path.split('_')[0]}_{prev_month}.csv' 

# classes dos controladores
bingManager = BingController()
sheets = SheetController()

# recuperando as campanhas de cada arquivos
current_campaigns = bingManager.findCampaigns(file_path)
prev_campaigns = bingManager.findCampaigns(prev_path)

# criaçao do pagina e header da midia
bing_page = sheets.createSheet('Bing')
sheets.createRow(['Bing Ads'])

for index, (current_campaign, prev_campaign) in enumerate(zip(current_campaigns, prev_campaigns)):
    with open(file_path, 'r') as file:
        campaigns = bingManager.findCampaigns(file)

    with open(prev_path, 'r') as file:
        prev_campaigns = bingManager.findCampaigns(file)

    current = []

    for index, campaign in campaigns.iterrows():
        campaign = bingManager.processCampaign(campaign, file_path)
        current = campaign

        sheets.createRow([campaign['name']])
        sheets.createRow(['Mes','Investimento','Impressoes','Cliques','CPC','CTR'])
        sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR']])
        sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR'], 'aaa'])

        for index, campaign in prev_campaigns.iterrows():
            campaign = bingManager.processCampaign(campaign, file_path)
            if(campaign['name'] == current['name']):
                print('igual')
                sheets.createRow([campaign['month'], f'R$ {str(campaign['investiment']).replace('.',',')}', campaign['impressions'], campaign['clicks'], f'R$ {str(campaign['CPC']).replace('.',',')}', campaign['CTR'], 'aaa'])

    # sheets.createRow([''])


        