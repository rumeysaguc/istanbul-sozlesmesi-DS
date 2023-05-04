import tweepy
import pandas as pd
import pytz
import datetime

# Twitter API bilgileri
consumer_key = "ukC1eP3Epq43gIYwbBq4knLXF"
consumer_secret = "e6uTMsSgual31w5EfR1n5kfvN9ZqKoj15WgoPLsk0BBD8LZDhX"
access_token = "2815936960-mS7TT9j5uQ5B12Zfr5rS1nd5E0Ugsh0HZSODjN4"
access_token_secret = "H2P2ZyIM1G2Nt8dwBZvpiuBNrr1VBOC72BZvRyhyB9nm1"

# Tweepy API objesi oluşturma
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Aranacak kelimeleri ve tarih aralığını belirleme
search_words = ['python', 'kod']
query = ' OR '.join(search_words)
since_date = datetime.datetime(2022, 5, 1, 0, 0, 0, tzinfo=pytz.UTC)
until_date = datetime.datetime(2022, 5, 4, 0, 0, 0, tzinfo=pytz.UTC)

# Tweetleri çekme
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='tr', count=100).items():
    if tweet.created_at < since_date:
        break
    if tweet.created_at > until_date:
        continue
    if tweet.in_reply_to_status_id is not None:
        continue
    tweets.append(tweet)

# Tweetleri Pandas DataFrame'e dönüştürme
data = []
for tweet in tweets:
    data.append([tweet.user.name, tweet.user.location, str(tweet.created_at.date()), tweet.text, tweet.user.verified,
                 tweet.retweet_count, tweet.favorite_count, tweet.source])
df = pd.DataFrame(data, columns=['username', 'location', 'created_at', 'tweet', 'blueTick', 'retweetCount',
                                 'favoriteCount', 'source'])
print(df.head())