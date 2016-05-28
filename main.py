# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path


with open('secrets.json') as data_file:    
    data = json.load(data_file)

    consumer_key = data['twitter_consumer_key']
    consumer_secret = data['twitter_consumer_secret']

    token_key = data['twitter_token_key']
    token_secret = data['twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    
    cursor = -1
    if os.path.isfile('cursor.txt'):
        cursor = open('cursor.txt').read()

    response = twitter.get_followers("bonobos", cursor=cursor)

    followers = response['users']
    next_cursor = response['next_cursor']


    with open('cursor.txt', 'w') as f:
       f.write("{}".format(next_cursor))

    with open('followers.json', 'a') as f:
       f.write("{}\n".format(json.dumps(followers)))
