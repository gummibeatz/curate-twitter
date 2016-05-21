# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
from follower_parser import FollowerParser
import json
import os.path


with open('/Volumes/LINUS_USB/Twitter-Scraper/secrets.json') as data_file:    
    data = json.load(data_file)

    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']

    token_key = data['token_key']
    token_secret = data['token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    
    line_number = 0
    if os.path.isfile('/Volumes/LINUS_USB/Twitter-Scraper/line_number'):
        line_number = open('/Volumes/LINUS_USB/Twitter-Scraper/line_number').read()

    list_index = 0
    if os.path.isfile('/Volumes/LINUS_USB/Twitter-Scraper/list_index'):
        list_index = open('/Volumes/LINUS_USB/Twitter-Scraper/list_index').read()

    # go through each user
    # save row at which you are at
    # save index of list that you are at
    # stop after 100 requests
    filename = '/Volumes/LINUS_USB/Twitter-Scraper/followers.json'

    parser = FollowerParser(line_number, filename)
    follower = parser.get_follower(list_index)
    print(follower.name())
