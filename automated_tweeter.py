# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path
import sys
import io
from unicode_csv import *


csv_filename = "test.csv"
csv_index_filename = "csv_index.txt"
secrets_filename = "secrets/automated_tweeter_secrets.json"
tweet_count=2

with open(secrets_filename) as data_file:    
    data = json.load(data_file)

    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']

    token_key = data['twitter_token_key']
    token_secret = data['twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    
    csv_index = 0
    if os.path.isfile(csv_index_filename):
        csv_index = open(csv_index_filename).read()

    with io.open(csv_filename, 'rb') as csv_data:
	reader = UnicodeReader(csv_data)
	for line_number, row in enumerate(reader):
            if line_number >= csv_index and line_number < csv_index + tweet_count:
                twitter.post_status(row[0] + row[1])

            if line_number == csv_index+tweet_count:
                break

    with open(csv_index_file, 'w') as f:
        f.write("{}".format(csv_index+tweet_count)) 
	   

