from openpyxl import Workbook
from openpyxl.styles import PatternFill, Alignment, Font

class SheetController:
    def __init__(self):
        self.workbook = Workbook()
        self.active_sheet = None

    def createSheet(self, titulo: str = ''):
        new_sheet = self.workbook.create_sheet(titulo)
        self.workbook.active = new_sheet
        self.active_sheet = new_sheet

        return new_sheet
    
    def setHeader(self, starting_cell, end_cell):
        self.active_sheet.merge_cells(f'{starting_cell}:{end_cell}')
        header = self.active_sheet[starting_cell]
        header.alignment =  Alignment(vertical='center', horizontal='center')
        header.fill = PatternFill('solid', fgColor='4f24ee')
        header.font = Font(name='Space Grotesk', b=True, color='FFFFFF')

    def createCampaignView(self, current_campaign: [], prev_campaign: [], ):
        sheet = self.active_sheet
        sheet.appen(current_campaign)
        sheet.appen(prev_campaign)

    def createRow(self, columns: []):
        self.active_sheet.append(columns)

    def save(self):
        self.workbook.save('./sheets/dados.xlsx')