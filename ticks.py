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
# TicksQueryType.AllDay 抓交易日期全天tick資料
ticks = api.ticks(
    contract=api.Contracts.Stocks["3419"], #指定要抓ticks資料的Contract
    date="2021-12-08", #交易日期
    query_type=sj.constant.TicksQueryType.RangeTime, #指定QueryType為RangeTime
    time_start="09:00:00", #開始時間
    time_end="09:05:00" #結束時間
)
# TicksQueryType.LastCount 抓交易日期最後X筆tick資料
'''last_5_ticks = api.ticks(
    contract=api.Contracts.Stocks["2330"], #指定要抓ticks資料的Contract
    date="2021-09-17", #交易日期
    query_type=sj.constant.TicksQueryType.LastCount, #指定QueryType為LastCount
    last_cnt=5 #指定要抓最後5筆tick資料
)'''
df = pd.DataFrame({**ticks}) #先將Ticks物件轉換為Dict，再傳入DataFrame做轉換
df.ts = pd.to_datetime(df.ts) #將原本的ts欄位中的資料，轉換為DateTime格式並回存
print(df) #將DataFrame的資料輸出至console中
api.logout()