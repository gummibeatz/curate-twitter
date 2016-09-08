# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
from pi_client import PersonalityInsightsAPI
from personality_insights_profile import PersonalityInsightsProfile
from twitter_follower import TwitterFollower
import json
import os.path
import io
import sys
from unicode_csv import *
from datetime import datetime

twitter_handle = sys.argv[-1]
line_number_file = "{0}/{1}_line_number.txt".format(twitter_handle, twitter_handle)
followers_file = "{0}/{1}_followers.json".format(twitter_handle, twitter_handle)
csv_file = "{0}/{1}_results.csv".format(twitter_handle, twitter_handle)
secrets_file = "secrets/{0}_secrets.json".format(twitter_handle)

with open(secrets_file) as secrets:    
    data = json.load(secrets)

    consumer_key = data['get_user_tweets_twitter_consumer_key']
    consumer_secret = data['get_user_tweets_twitter_consumer_secret']

    token_key = data['get_user_tweets_twitter_token_key']
    token_secret = data['get_user_tweets_twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)

    line_number = 0
    if os.path.isfile(line_number_file):
        line_number = int(open(line_number_file).read())

    with io.open(csv_file, 'ab') as csv_data:
        writer = UnicodeWriter(csv_data)

        with open(followers_file, 'r') as followers:
            for i, line in enumerate(followers):
                if i < line_number:
                    continue
                elif i == line_number:
                    follower = TwitterFollower(json.loads(line))
                    
                    tweets =  twitter.get_user_timeline(follower.screen_name())

                    # we should separate out tweet per line, as json
                    # then save each of these tweets in a txt file called #{username}.json 
                    # or some shit like that
                else:
                    break

    with open(line_number_file, 'w') as f:
        f.write("{}".format(line_number + 1))
