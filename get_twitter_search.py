# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path
import sys

query = sys.argv[-1]
secrets_file = "query_secrets/{0}_secrets.json".format(query)
tweets_filename = "twitter_queries/{0}.json".format(query)

with open(secrets_file) as secrets:
    data = json.load(secrets)

    consumer_key = data['twitter_consumer_key']
    consumer_secret = data['twitter_consumer_secret']

    token_key = data['twitter_token_key']
    token_secret = data['twitter_token_secret']

    print consumer_key
    print consumer_secret
    print token_key
    print token_secret

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)

    with open(tweets_filename, 'a+') as f:
        print "yay"

    print twitter.search(query)
