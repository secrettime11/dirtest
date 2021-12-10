from shioaji.data import Kbars
import pandas as pd
import shioaji as sj

api = sj.Shioaji()
api.login(
    person_id="M122603015",
    passwd="richman0104",
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done."))

kbars = api.kbars(api.Contracts.Stocks["3419"],  start="2021-12-08", end="2021-12-08", timeout = 30000)
df = pd.DataFrame({**kbars}) #先將Kbars物件轉換為Dict，再傳入DataFrame做轉換
df.ts = pd.to_datetime(df.ts) #將原本的ts欄位中的資料，轉換為DateTime格式並回存
df.head()
print(df)
#df.to_csv('Id3419.xls', index=False, encoding="utf_8_sig")