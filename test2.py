import tweepy
import csv
import pandas as pd
import json
import datetime
from json import JSONEncoder


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


created_on = datetime.datetime.now()

####input your credentials here
consumer_key = "ukC1eP3Epq43gIYwbBq4knLXF"
consumer_secret = "e6uTMsSgual31w5EfR1n5kfvN9ZqKoj15WgoPLsk0BBD8LZDhX"
access_token = "2815936960-mS7TT9j5uQ5B12Zfr5rS1nd5E0Ugsh0HZSODjN4"
access_token_secret = "H2P2ZyIM1G2Nt8dwBZvpiuBNrr1VBOC72BZvRyhyB9nm1"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
data =[]
queryTopics = 'istanbul sözleşmesi or "kadın hakları"'
for tweet in tweepy.Cursor(api.search_tweets,q=queryTopics,count=100,
                           lang="tr",
                           since="2017-04-03").items():
    data.append([ tweet.user.name, 
                                                tweet.user.location,\
                                               str(tweet.created_at.date()),
                                            tweet.text,
                                            tweet.retweet_count,
                                            tweet.favorite_count, 
                                             tweet.source])
    print (tweet.created_at, tweet.text)
df = pd.DataFrame(data, columns=['username','location','created_at','tweet','retweetCount','favoriteCount','source'])
print(df.head())
df.to_excel("all2.xlsx")