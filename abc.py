import os
import shioaji as sj
from dotenv import load_dotenv #從dotenv模組中匯入load_dotenv這個function
import pandas as pd #匯入pandas模組

load_dotenv() #讀取設定檔中的內容至環境變數
api = sj.Shioaji()

api.login(
    person_id=os.getenv('YOUR_PERSON_ID'),
    passwd=os.getenv('YOUR_PASSWORD'),
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)

contracts = [api.Contracts.Stocks['2330'],api.Contracts.Stocks['2890']]
short_stock_sources = api.short_stock_sources(contracts)
df = pd.DataFrame(short_stock_sources) #將short_stock_sources轉換為DataFrame
df.ts = pd.to_datetime(df.ts) #將原本的ts欄位中的資料，轉換為DateTime格式並回存
print(df)