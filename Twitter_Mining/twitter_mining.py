import json
import tweepy
from tweepy import OAuthHandler

def store(name,data):
    file = name + ".json"
    data = json.dumps(data)
    with open(file, 'w') as f:
        f.write(data)

def print(data):
    print(json.dumps(data))



consumer_key = 'BvxUlgkE8RYZqNstffsWWR7R7'
consumer_secret = 'zbdavSVCOKIPgpIvrJPudw54elFWtTGDQxfwtH1DRCiXYKt5xg'
access_token = '888084649-RYujdf9G4mMWoORK8Yg3YjOxaT8Zcw1QIkhxnUfk'
access_secret = 'jo4gr9iHdFuB77FEz5vTjOExHKZvQDDMuHLFVcLcQWfgc'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    store('timeline',status._json)

for friend in tweepy.Cursor(api.friends).items():
    store('followers',friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    store('my_tweets',tweet._json)
