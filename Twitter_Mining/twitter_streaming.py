from tweepy import OAuthHandler
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

with open("auth.json",'r') as f:
    f = json.load(f)

consumer_key = f['api_keys'][0]['consumer_key']
consumer_secret = f['api_keys'][0]['consumer_secret']
access_token = f['api_keys'][0]['access_token']
access_secret = f['api_keys'][0]['access_secret']


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
