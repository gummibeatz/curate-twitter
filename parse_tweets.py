# -*- coding: UTF-8 -*-

from tweet import Tweet 
import json
import os.path
import sys

query = sys.argv[-1]
tweets_filename = "twitter_queries/{0}.json".format(query)
tweets_csvs_filename = "twitter_queries_csvs/{0}.json".format(query)

with open(tweets_filename) as tweets_file:
    for search_object in tweets_file:
        search
        print tweet_data
        tweet = Tweet(tweet_data)
        print tweet.text
        break
    
