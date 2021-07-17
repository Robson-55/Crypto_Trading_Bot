#This code will take the data scrapped from both Reddit API and Coingecko API,  
#transform and process it in order to get a unified dataframe which will be finally  
#processed by the LSTM neural network in order to make the predictions.  

#Import libraries
import pandas as pd
import transformers
from transformers import pipeline

# Importing Data
# Importing Reddit posts
df_posts = pd.read_csv(
    "C:/Users/rober/Desktop/MIS COSAS/DSTI MASTER/SUBJECTS/PYTHON LABS/Crypto Trading Bot/Crypto_Trading_Bot-main/Crypto_Trading_Bot-main/Reddit_Scrapper/subreddit-comments-dl/dataset/finals/concat_file.csv")
print(df_posts.head())
print(df_posts.info())
# Importing financial data of cryptocurrencies (prices, volumes)
df_prices = pd.read_csv(
    "C:/Users/rober/Desktop/MIS COSAS/DSTI MASTER/SUBJECTS/PYTHON LABS/Crypto Trading Bot/prices.csv")
df_prices=df_prices.iloc[:,1:3]

#df_prices=df_prices.reindex(columns=['Timestamp','total_volumes','prices'])
print(df_prices.head())
print(df_prices.info())

# Performing sentiment analysis through transformer pipeline, which uses as default the model: distilbert-base-cased
sentiment_analyzer = pipeline('sentiment-analysis')
sentiment_score = sentiment_analyzer("bitcoin is as useful as if my fish managed the global economy")
print(type(sentiment_score))
print(sentiment_score)
print(sentiment_score[0]["label"])
if sentiment_score[0]["label"] == "NEGATIVE":
    sentiment_score[0]["score"] = 1 - sentiment_score[0]["score"]
print(sentiment_score[0]["score"])


# Function for performing sentiment analysis scoring with distilbert-base-cased model from transformers library
def scorer(text):
    text = str(text)
    # sentiment_analyzer = pipeline('sentiment-analysis')
    sentiment_score = sentiment_analyzer(text)
    if sentiment_score[0]["label"] == "NEGATIVE":
        sentiment_score[0]["score"] = 1 - sentiment_score[0]["score"]
    return sentiment_score[0]["score"]


print(df_posts.loc[1])
print(df_posts.loc[1][1])
print(len(df_posts.columns))

print(scorer(df_posts.loc[1][1]))


# Function for transforming all posts to scores
def posts_to_scores(dataframe):
    for i in range(len(dataframe)):
        for j in range(1, len(dataframe.columns)):
            dataframe.loc[i][j] = scorer(dataframe.loc[i][j])
            j = j + 1
        i = i + 1


posts_to_scores(df_posts)
print(df_posts.head())

# Averaging scores for each row
cols=df_posts.iloc[:,1:]
df_posts['Sentiment Mean'] = cols.mean(axis=1)
print(df_posts.head())
df_posts_averaged = df_posts[['index', 'Sentiment Mean']]
print(df_posts_averaged.head())
df_posts_averaged.columns = ['Timestamp', 'Sentiment Mean']
df_posts = df_posts.astype({"Timestamp": str})
print(df_posts_averaged.head())
# Generating a single dataframe with both financial data (df_prices) and sentiment scores (df_posts) by date merging.
df_final=pd.merge(df_posts_averaged,df_prices, how='outer',on='Timestamp')
print("DF FINAL")
print(df_final.head())


df_final.to_csv("df_final.csv")
