# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path
import sys
import io
from unicode_csv import *


csv_file = "test.csv"
csv_index_file = "csv_index.txt"
secrets_file = "secrets/automated_tweeter_secrets.json"
tweet_count=2

with open(secrets_file) as data_file:    
    data = json.load(data_file)

    consumer_key = data['twitter_consumer_key']
    consumer_secret = data['twitter_consumer_secret']

    token_key = data['twitter_token_key']
    token_secret = data['twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    
    csv_index = 0
    if os.path.isfile(csv_index_file):
        csv_index = open(csv_index_file).read()

    with io.open(csv_file, 'rb') as csv_data:
	reader = UnicodeReader(csv_data)
	for line_number, row in enumerate(reader):
            if line_number >= csv_index and line_number < csv_index + tweet_count:
                status = row[0] + row[1]
                print "posting status: {0}".format(status)
                twitter.post_status(status)

            if line_number == csv_index+tweet_count:
                break

    with open(csv_index_file, 'w+') as f:
        f.write("{}".format(csv_index+tweet_count)) 
	   

