import requests
from requests_oauthlib import OAuth1
from json import JSONEncoder
import json
import datetime

class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

# API anahtarları
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# Tarih aralığı
start_date = "2022-01-01"
end_date = "2023-01-31"

# Aranacak hashtag
hashtag = "istanbul"

# Twitter Search API endpointi
url = "https://api.twitter.com/1.1/search/tweets.json"

# Arama parametreleri
params = {
    "q": f"#{hashtag}",
    "lang": "tr",
    "count": 100,
    "result_type": "recent",
    "tweet_mode": "extended",
    "since_id": start_date,
    "max_id": end_date,
}
try:
    # OAuth1 kimlik doğrulama
    auth = OAuth1(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
except Exception as ex:
    print(ex)
x= 5
# Search API'ye istek gönderme
response = requests.get(url, params=params, auth=auth)
print(response)
# Yanıtı JSON'a dönüştürme
data = response.json()
fileName = 'allData' + '.json'
outfile1 = open(fileName, 'w')
json.dump(data, outfile1, cls=DateTimeEncoder)

# Tweetleri yazdırma
for tweet in data["statuses"]:
    print(tweet["full_text"])
