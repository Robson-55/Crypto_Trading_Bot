#Coingecko is a web where people can find cryptocurrency market data and historics.
#By using Coingecko API this data can be retrieved and stores, for its later processing and use.

#Importing Libraries
import pycoingecko
from pycoingecko import CoinGeckoAPI
import pandas as pd
import os.path as path
import glob

#Defining relative paths
one_up = path.abspath(path.join(__file__ ,".."))
two_up =  path.abspath(path.join(__file__ ,"../.."))
three_up =  path.abspath(path.join(__file__ ,"../../.."))

#Initializing coingecko API and using it to extract information about "Ethereum" cryptocurrency.

cg = CoinGeckoAPI()
x=cg.get_price(ids='ethereum', vs_currencies='usd',include_market_cap='true')

#Storing it in a pandas dataframe
df2 = pd.DataFrame(data=x)

#Pushing it to a csv file
df2.to_csv(one_up + "/CSV/cg_get_price.csv",index=False)
print(x)

#Getting Ethereum data from Coingecko API for a certain time range given in timestamp format. 
#For converting timestamp to date format it can be used https://www.epochconverter.com/
y=cg.get_coin_market_chart_range_by_id(id='ethereum',vs_currency='usd',include_24hr_vol='true' ,include_24hr_change='true', from_timestamp='1500000000',to_timestamp='1623715200')
print(y)
#Storing data into a dataframe
df = pd.DataFrame(data=y)
#Exporting dataframe to csv file
df.to_csv(one_up + "/CSV/cg_dataframe.csv",index=False)
print(df.head())

#Geting a new dataframe with certain columns
df1 = pd.DataFrame([df['prices'].str[0], df['prices'].str[1], df['total_volumes'].str[1]]).transpose()
#Changing column name
df1.columns.values[0] = "Timestamp"
#Transforming timestamp to datetime format
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], unit='ms')
#Exporting dataframe to csv file
df1.to_csv(one_up + "/CSV/cg_dataframe_timestamps.csv",index=False)
#Some info about this dataframe
print(df1.head())

