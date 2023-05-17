import tweepy
import csv
import pandas as pd
import json
import datetime
from json import JSONEncoder
import pytz


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


created_on = datetime.datetime.now()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
data =[]


turkey = pytz.timezone('Europe/Istanbul')

since_id = turkey.localize(datetime.datetime(2019, 1, 1, 0, 0, 0))
until_id = turkey.localize(datetime.datetime(2020, 1, 31, 23, 59, 59))
search_words = ['python', 'kod']
query = ' OR '.join(search_words) + ' -filter:retweets'
data = []
for tweet in tweepy.Cursor(api.search, q=query, count=100, lang='tr', tweet_mode='extended', since_id=since_id, until_id=until_id).items():
    if tweet.created_at < since_id:
        break
    if tweet.created_at > until_id:
        continue
    if tweet.in_reply_to_status_id is not None:
        continue
    data.append([tweet.user.name, 
                 tweet.user.location,
                 str(tweet.created_at.date()),
                 tweet.full_text, 
                 tweet.user.verified,
                 tweet.retweet_count,
                 tweet.favorite_count, 
                 tweet.source])
    print(tweet.created_at, tweet.full_text)
df = pd.DataFrame(data, columns=['username','location','created_at','tweet','blueTick','retweetCount','favoriteCount','source'])
print(df.head())
filename = str(created_on.date()) +'.xlsx'
df.to_excel(filename)
