import tweepy as tw
import pandas as pd
import datetime
# your Twitter API key and API secret
my_api_key = ""
my_api_secret = ""
created_on = datetime.datetime.now()

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = "#istanbulsözleşmesiyaşatır -filter:retweets"

# set date range
since_date = "2020-03-01"
until_date = "2023-05-06"

# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
                   q=search_query,
                   lang="tr",
                   since=since_date,
                   until=until_date).items(100)

# store the API responses in a list
tweets_copy = [tweet for tweet in tweets]

print("Total Tweets fetched:", len(tweets_copy))

# populate the dataframe
test = []
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    test.append({'user_name': tweet.user.name,
                 'user_location': tweet.user.location,\
                 'user_description': tweet.user.description,
                 'user_verified': tweet.user.verified,
                 'date': tweet.created_at,
                 'text': text,
                 'hashtags': [hashtags if hashtags else None],
                 'source': tweet.source})

# create dataframe
df_extended = pd.DataFrame(test, columns=['user_name', 'user_location', 'user_description', 'user_verified', 'date', 'text', 'hashtags', 'source'])
print(df_extended.head())
filename = str(created_on.date()) +'.xlsx'
df_extended.to_excel(filename)
