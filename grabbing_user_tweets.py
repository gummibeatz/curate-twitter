# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
from pi_client import PersonalityInsightsAPI
from follower_parser import FollowerParser
from personality_insights_profile import PersonalityInsightsProfile
import json
import os.path
import csv
import io
from unicode_csv import *

def assemble_profile_from_tweets(tweets):
    formatted_tweets = []
    ct = 0
    for tweet in tweets:
        formatted_tweets.append({
            "content": tweet['text'],
            "contenttype": "text/plain",
            "created": 0,
            "id":tweet['id_str'],
            "language": "en",
            "sourceid": "Twitter API",
            "userid": "@wouldn'tyouliketoknow"
        })
    return {"contentItems": formatted_tweets}


with open('secrets.json') as data_file:    
    data = json.load(data_file)

    consumer_key = data['twitter_consumer_key']
    consumer_secret = data['twitter_consumer_secret']

    token_key = data['twitter_token_key']
    token_secret = data['twitter_token_secret']

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)

    pi_username = data['pi_username']
    pi_password = data['pi_password']

    pi = PersonalityInsightsAPI(pi_username, pi_password)

    line_number = 0
    if os.path.isfile('line_number'):
        line_number = open('line_number').read()

    list_index = 0
    if os.path.isfile('list_index'):
        list_index = open('list_index').read()

    # go through each user
    # save row at which you are at
    # save index of list that you are at
    # stop after 100 requests
    filename = 'followers.json'

    parser = FollowerParser(line_number, filename)
    
    csv_filename = 'results.csv'

    with io.open(csv_filename, 'wb') as csv_data:
        writer = UnicodeWriter(csv_data)

        for i in range(list_index, list_index + 100):
            follower = parser.get_follower(i)
            
            tweets =  twitter.get_user_timeline(follower.screen_name())
            profile = assemble_profile_from_tweets(tweets)
            pi_profile = PersonalityInsightsProfile(pi.get_profile(profile))
            print(pi_profile.adventurousness().percentage())
            writer.writerow([
                follower.name(),
                follower.screen_name(),
                follower.location(),
                follower.followers_count(),
                follower.friends_count(),
                follower.statuses_count()
            ])
            break
