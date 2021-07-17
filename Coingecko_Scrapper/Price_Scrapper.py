import pycoingecko
from pycoingecko import CoinGeckoAPI
import pandas as pd
import os.path as path
import glob

one_up = path.abspath(path.join(__file__ ,".."))
two_up =  path.abspath(path.join(__file__ ,"../.."))
three_up =  path.abspath(path.join(__file__ ,"../../.."))


cg = CoinGeckoAPI()
x=cg.get_price(ids='ethereum', vs_currencies='usd',include_market_cap='true')
df2 = pd.DataFrame(data=x)
df2.to_csv(one_up + "/CSV/cg_get_price.csv",index=False)
print(x)

y=cg.get_coin_market_chart_range_by_id(id='ethereum',vs_currency='usd',include_24hr_vol='true' ,include_24hr_change='true', from_timestamp='1500000000',to_timestamp='1623715200')
print(y)
df = pd.DataFrame(data=y)
df.to_csv(one_up + "/CSV/cg_dataframe.csv",index=False)
print(df.head())

df1 = pd.DataFrame([df['prices'].str[0], df['prices'].str[1], df['total_volumes'].str[1]]).transpose()
df1.columns.values[0] = "Timestamp"
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], unit='ms')
df1.to_csv(one_up + "/CSV/cg_dataframe_timestamps.csv",index=False)

print(df1.head())

