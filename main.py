# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path


with open('/Volumes/LINUS_USB/Twitter-Scraper/secrets.json') as data_file:    
    data = json.load(data_file)

    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']

    token_key = data['token_key']
    token_secret = data['token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    
    cursor = -1
    if os.path.isfile('/Volumes/LINUS_USB/Twitter-Scraper/cursor.txt'):
        cursor = open('/Volumes/LINUS_USB/Twitter-Scraper/cursor.txt').read()

    response = twitter.get_followers("bonobos", cursor=cursor)

    followers = response['users']
    next_cursor = response['next_cursor']


    with open('/Volumes/LINUS_USB/Twitter-Scraper/cursor.txt', 'w') as f:
       f.write("{}".format(next_cursor))

    with open('/Volumes/LINUS_USB/Twitter-Scraper/followers.json', 'a') as f:
       f.write("{}\n".format(json.dumps(followers)))
