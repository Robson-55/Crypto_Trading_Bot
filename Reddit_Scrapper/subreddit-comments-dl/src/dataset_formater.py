import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import datetime
from datetime import datetime
import glob
import os.path as path
one_up = path.abspath(path.join(__file__ ,".."))
two_up =  path.abspath(path.join(__file__ ,"../.."))
three_up =  path.abspath(path.join(__file__ ,"../../.."))


df = pd.read_csv(two_up + '/dataset/20210717182858/submissions.csv')

# Format datetime
df.created_utc = pd.to_numeric(df.created_utc)
df['created_utc'] = df['created_utc'].astype(int)
df["created_utc"] = df["created_utc"].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%d-%m-%Y'))

# Sort by date & most upvoted
df = df.sort_values(["created_utc","score"], ascending = (True, False))

# Group by same day and filter to only have top10 most upvoted per day
df = df.groupby('created_utc').head(10)

# Transpose and allow for top10 comments per day to be 10 columns per day
days = df['created_utc'].unique()
daily_df = []
for i in days:
  i_df = df.loc[df['created_utc'] == i]
  i_df = i_df.reset_index(drop=True)
  i_df['inx'] = i_df.index + 1
  in_df = i_df.pivot(index='created_utc',
          columns='inx',
          values='title')
  daily_df.append(in_df)
   
final_df = pd.concat(daily_df)

final_df['index'] = final_df.index
column_names = ["index",1, 2, 3,4, 5, 6,7, 8, 9, 10]
final_df = final_df.reindex(columns=column_names)
final_df["index"] = pd.to_datetime(final_df["index"])
final_df = final_df.sort_values(by="index")

final_df.to_csv(two_up + "/dataset/finals/concat_file.csv",index=False)

