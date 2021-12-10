from dotenv import load_dotenv
import os
import shioaji as sj
import pandas as pd
from shioaji import TickSTKv1, Exchange #從shioaji模組，匯入TickSTKv1及Exchange物件
from threading import Event #threading模組，匯入Event物件

load_dotenv() #讀取設定檔中的內容至環境變數

api = sj.Shioaji()
api.login(
    person_id=os.getenv('YOUR_PERSON_ID'), 
    passwd=os.getenv('YOUR_PASSWORD')
)