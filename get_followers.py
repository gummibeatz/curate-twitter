# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path
import sys

twitter_handle = sys.argv[-1]
cursor_txt_filename = "{0}/{1}_cursor.txt".format(twitter_handle, twitter_handle)
followers_filename = "{0}/{1}_followers.json".format(twitter_handle, twitter_handle)
secrets_file = "secrets/{0}_secrets.json".format(twitter_handle)

with open(secrets_file) as data_file:    
    data = json.load(data_file)

    consumer_key = data['get_followers_twitter_consumer_key']
    consumer_secret = data['get_followers_twitter_consumer_secret']

    token_key = data['get_followers_twitter_token_key']
    token_secret = data['get_followers_twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    
    cursor = -1
    if os.path.isfile(cursor_txt_filename):
        cursor = open(cursor_txt_filename).read()

    response = twitter.get_followers(twitter_handle, cursor=cursor)

    followers = response['users']
    next_cursor = response['next_cursor']

    with open(cursor_txt_filename, 'w') as f:
       f.write("{}".format(next_cursor))

    with open(followers_filename, 'a') as f:
       f.write("{}\n".format(json.dumps(followers)))
