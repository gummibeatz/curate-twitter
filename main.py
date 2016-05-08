from twitter_client import TwitterAPI
import json


with open('secrets.json') as data_file:    
    data = json.load(data_file)

    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']

    token_key = data['token_key']
    token_secret = data['token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    response = twitter.get_followers("bonobos")

    followers = response['users']
    next_cursor = response['next_cursor']


    with open('cursor.txt', 'w') as f:
       f.write("{}".format(next_cursor))

    with open('bonobos_followers.json', 'a') as f:
        f.write("{}".format(followers))
