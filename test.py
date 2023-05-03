import tweepy as tw
# your Twitter API key and API secret
my_api_key = "ukC1eP3Epq43gIYwbBq4knLXF"
my_api_secret = "e6uTMsSgual31w5EfR1n5kfvN9ZqKoj15WgoPLsk0BBD8LZDhX"
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = "#istanbulsozlesmesi -filter:retweets"
# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
q=search_query,
              lang="tr",
              since="2020-09-16").items(50)
# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
    
print("Total Tweets fetched:", len(tweets_copy))

import pandas as pd
# intialize the dataframe
tweets_df = pd.DataFrame()
test = []
text =""
# populate the dataframe

for tweet in tweets_copy:
    hashtags = []
    if tweet:
        try:
            for hashtag in tweet.entities["hashtags"]:
                hashtags.append(hashtag["text"])
            text = api.get_status(id=tweet.id, tweet_mode='popular').full_text
        except:
            pass
    
        test = test.append(pd.DataFrame({'user_name': tweet.user.name, 
                                                'user_location': tweet.user.location,\
                                                'user_description': tweet.user.description,
                                                'user_verified': tweet.user.verified,
                                                'date': tweet.created_at,
                                                'text': text, 
                                                'hashtags': [hashtags if hashtags else None],
                                                'source': tweet.source}))
   # test = test.reset_index(drop=True)
# show the dataframe
df_extended = pd.DataFrame(test, columns=['A', 'B', 'C','A', 'B', 'C','A', 'B'])
print(df_extended.head())