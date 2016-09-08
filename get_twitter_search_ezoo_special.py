# -*- coding: UTF-8 -*-

# gets twitter query based on command line preference
from twitter_client import TwitterAPI
import json
import os.path
import sys

query = '#ezoo' 
secrets_file = "query_secrets/{0}_secrets.json".format(query)
tweets_filename = "twitter_queries/{0}.json".format(query)
max_id_filename = "twitter_queries/{0}_max_id.txt".format(query)

with open(secrets_file) as secrets:
    data = json.load(secrets)

    consumer_key = data['twitter_consumer_key']
    consumer_secret = data['twitter_consumer_secret']

    token_key = data['twitter_token_key']
    token_secret = data['twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)

with open(tweets_filename, 'a+') as f:
    tweets = twitter.search(query)['statuses']
    for tweet in tweets:
        f.write("{}\n".format(json.dumps(tweets)))
