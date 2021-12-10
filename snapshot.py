from dotenv import load_dotenv
import os
import shioaji as sj
import pandas as pd

load_dotenv() #讀取設定檔中的內容至環境變數

api = sj.Shioaji()
api.login(
    person_id=os.getenv('YOUR_PERSON_ID'), 
    passwd=os.getenv('YOUR_PASSWORD')
)


contracts = [api.Contracts.Stocks['2330'], api.Contracts.Stocks['2890']]
snapshots = api.snapshots(contracts)
print(snapshots[0])