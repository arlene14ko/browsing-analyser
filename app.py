import sys
from datetime import datetime
from utils import Utils


browser = Utils.get_browserhistory()
#print(browser)
Utils.write_browserhistory_csv()