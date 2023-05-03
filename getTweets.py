import configparser
import tweepy
import pandas as pd
# Read the config file

from openpyxl import Workbook

config = configparser.RawConfigParser()
config.read('config.ini')

api_key = "ukC1eP3Epq43gIYwbBq4knLXF"
api_key_secret = "e6uTMsSgual31w5EfR1n5kfvN9ZqKoj15WgoPLsk0BBD8LZDhX"
access_token = "2815936960-mS7TT9j5uQ5B12Zfr5rS1nd5E0Ugsh0HZSODjN4"
access_token_secret = "H2P2ZyIM1G2Nt8dwBZvpiuBNrr1VBOC72BZvRyhyB9nm1"
# Read the values
#api_key = config['twitter']['api_key']
#api_key_secret = config['twitter']['api_key_secret']
#bearer_token = "AAAAAAAAAAAAAAAAAAAAABqwnAEAAAAA6E9eil5dENcQoGs8NS3M6sxqlzc%3DSRRwQ1J7CCZgjUJ3pO2IrcpGVV4K4EYJUUVM6jkPRliBPuIuM5"
#access_token = config['twitter']['access_token']
#access_token_secret = config['twitter']['access_token_secret']
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
limit =10
hashtag = "istanbulsozlesmesi"

columns = ['User', 'Tweet', 'Likes', 'Retweets', 'Date']
data = []

try:
    api.verify_credentials()
    print('Successful Authentication')
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=hashtag, lang = "tr", count=15).items(5)
        #print(type(tweets))
        
        for tweet in tweets:
            print(tweet.user.name,tweet.id,tweet.created_at,tweet.favorite_count, tweet.retweet_count)
            try:
                data.append([tweet.user.screen_name,tweet.text.encode('utf-8'),tweet.retweeted_status.favorite_count, tweet.retweet_count, str(tweet.created.date())])
            except: 
                data.append([tweet.user.screen_name, tweet.text.encode('utf-8'), tweet.favorite_count, tweet.retweet_count, str(tweet.created_at.date())])    

    except Exception as ex:
        print(ex)
except:
    print('Failed authentication')

df = pd.DataFrame(data, columns=columns)
df.to_excel("Cup2022.xlsx")