import json
import tweepy
from tweepy import OAuthHandler

def store(name,data):
    file = name + ".json"
    data = json.dumps(data)
    with open(file, 'w') as f:
        f.write(data)

def printing(data):
    print(json.dumps(data))

with open("auth.json",'r') as f:
    f = json.load(f)

consumer_key = f['api_keys'][0]['consumer_key']
consumer_secret = f['api_keys'][0]['consumer_secret']
access_token = f['api_keys'][0]['access_token']
access_secret = f['api_keys'][0]['access_secret']


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    store('timeline',status._json)

for friend in tweepy.Cursor(api.friends).items():
    store('followers',friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    store('my_tweets',tweet._json)
