import pycoingecko
from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
x=cg.get_price(ids='ethereum', vs_currencies='usd',include_market_cap='true')
print(x)

y=cg.get_coin_market_chart_range_by_id(id='ethereum',vs_currency='usd',from_timestamp='1610668800',to_timestamp='1623715200')
print(y)
df = pd.DataFrame(data=y)

print(df.head())

df1 = pd.DataFrame([df['prices'].str[0], df['prices'].str[1], df['total_volumes'].str[1]]).transpose()
df1.columns.values[0] = "Timestamp"
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], unit='ms')
print(df1.head())

