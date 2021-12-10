from dotenv import load_dotenv
import os
import shioaji as sj
import pandas as pd
from shioaji import TickSTKv1, Exchange #從shioaji模組，匯入TickSTKv1及Exchange物件
from threading import Event, Thread #threading模組，匯入Event物件
import time

load_dotenv() #讀取設定檔中的內容至環境變數

api = sj.Shioaji()
api.login(
    person_id=os.getenv('YOUR_PERSON_ID'), 
    passwd=os.getenv('YOUR_PASSWORD')
)


#訂閱個股盤中tick資訊
api.quote.subscribe(
    api.Contracts.Stocks["3508"], 
    quote_type = sj.constant.QuoteType.Tick, # or 'tick'
    version = sj.constant.QuoteVersion.v1 # or 'v1'
)
api.quote.subscribe(
    api.Contracts.Stocks["6243"], 
    quote_type = sj.constant.QuoteType.Tick, # or 'tick'
    version = sj.constant.QuoteVersion.v1 # or 'v1'
)
api.quote.subscribe(
    api.Contracts.Stocks["6443"], 
    quote_type = sj.constant.QuoteType.Tick, # or 'tick'
    version = sj.constant.QuoteVersion.v1 # or 'v1'
)
api.quote.subscribe(
    api.Contracts.Stocks["3419"], 
    quote_type = sj.constant.QuoteType.Tick, # or 'tick'
    version = sj.constant.QuoteVersion.v1 # or 'v1'
)

api.quote.subscribe(
    api.Contracts.Stocks["4503"], 
    quote_type = sj.constant.QuoteType.Tick, # or 'tick'
    version = sj.constant.QuoteVersion.v1 # or 'v1'
)

Event().wait() #盤中執行程式時，若看不到quote_callback的執行結果，請加入此行
# 定義quote_callback，即回傳報價資訊時所要執行的動作
@api.on_tick_stk_v1()
def quote_callback(exchange: Exchange, tick:TickSTKv1):
    print(f"Exchange: {exchange}, Tick: {tick}") #將報價資訊內容輸出至console中