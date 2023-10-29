month = '09'

# controllers
from controllers.SheetController import SheetController
from controllers.Processors import Processors

sheets = SheetController()
processors = Processors()


processors.run_bing(sheets, file_path=f'./csv/bing_{month}.csv')
processors.run_linkedin(sheets, file_path=f'./csv/linkedin_{month}.csv')

sheets.save()