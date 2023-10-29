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


sheets.save()