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

max_id = int(open(max_id_filename).read())

with open(tweets_filename, 'a+') as f:
    search = twitter.search(query, max_id=max_id)
    tweets = search['statuses']
    for tweet in tweets:
        f.write("{}\n".format(json.dumps(tweet)))

with open(max_id_filename, 'w+') as f:
    last_tweet = tweets[-1]
    max_id = last_tweet['id_str']
    f.write(max_id)
