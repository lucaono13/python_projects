import json
"""
with open('my_tweets.json', 'r') as f:
    line = f.readline()
    tweet = json.loads(line)
    print(json.dumps(tweet,indent = 4))
"""
import nltk
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
tweet = 'RT @lucaono13: just an example! :D'
print(word_tokenize(tweet))
