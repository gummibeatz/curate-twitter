# -*- coding: UTF-8 -*-
#
# gets twitter followers for a particular twitter handles
# Usage: python get_followers.py potus
#
# resulting followers stored as one follower json object per line
# to TWITTERH_HANDLE/TWITTER_HANDLE_followers.json

from twitter_client import TwitterAPI
import simplejson as json
import os.path
import sys

def get_value_with_file(filename, default_value=0):
    cursor = default_value
    if os.path.isfile(filename):
        cursor = open(filename).read()

    return cursor

def set_value_to_file(filename, value):
    with open(filename, 'w') as f:
       f.write("{}".format(value))


def create_twitter_client(secrets_file):
    with open(secrets_file) as data_file:
        data = json.load(data_file)

        consumer_key = data['get_followers_twitter_consumer_key']
        consumer_secret = data['get_followers_twitter_consumer_secret']
        token_key = data['get_followers_twitter_token_key']
        token_secret = data['get_followers_twitter_token_secret']

        return TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)


#### Script Begins ####
twitter_handle = sys.argv[-1]
cursor_txt_file = "{0}/{1}_cursor.txt".format(twitter_handle, twitter_handle)
followers_file = "{0}/{1}_followers.json".format(twitter_handle, twitter_handle)
line_number_file = "{0}/{1}_following_line_number.txt".format(twitter_handle, twitter_handle)
secrets_file = "secrets/{0}_secrets.json".format(twitter_handle)

twitter = create_twitter_client(secrets_file)

cursor = get_value_with_file(cursor_txt_file, default_value=-1)
line_number = get_value_with_file(line_number_file)

response = twitter.get_followers(twitter_handle, cursor=cursor)

followers = response['users']
next_cursor = response['next_cursor']

set_value_to_file(cursor_txt_file, next_cursor)

with open(followers_filename, 'a') as f:
    for follower in followers:
        f.write("{}\n".format(json.dumps(follower)))
