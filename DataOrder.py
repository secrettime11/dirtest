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


ticks = api.ticks(
    contract=api.Contracts.Stocks["2330"], 
    date="2020-03-04"
)
ticks = pd.DataFrame(ticks)
ticks.to_csv('ticks.csv',index=False,encoding="utf_8_sig")
#print(ticks)

'''
# 取得當日價格變動範圍排行前五名個股資料
day_range_rank = api.scanners(
            scanner_type = sj.constant.ScannerType.AmountRank ,
            count = 5,
            date='2021-12-08'
          )
day_range_rank_df = pd.DataFrame(day_range_rank) #將day_range_rank資料轉換為DataFrame
day_range_rank_df.ts = pd.to_datetime(day_range_rank_df.ts)
# 透過to_csv將DataFrame匯出為csv檔
day_range_rank_df.to_csv('day_range_rank.csv', index=False, encoding="utf_8_sig")
'''