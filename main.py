from twitter_client import TwitterAPI
import json


with open('secrets.json') as data_file:    
    data = json.load(data_file)

    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']

    token_key = data['token_key']
    token_secret = data['token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    followers = twitter.get_followers("bonobos")["users"]
