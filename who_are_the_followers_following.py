# -*- coding: UTF-8 -*-

from twitter_client import TwitterAPI
import json
import os.path
import sys
from follower_parser import FollowerParser

twitter_handle = sys.argv[-1]
followers_file = "{0}/{1}_followers.json".format(twitter_handle, twitter_handle)
secrets_file = "secrets/{0}_secrets.json".format(twitter_handle)
line_number_file = "{0}/{1}_following_line_number.txt".format(twitter_handle, twitter_handle)
list_index_file = "{0}/{1}_following_list_index.txt".format(twitter_handle, twitter_handle)
who_followers_follow_file = "{0}/{1}_who_followers_follow.txt".format(twitter_handle, twitter_handle)

with open(secrets_file) as data_file:    
    data = json.load(data_file)

    consumer_key = data['who_are_the_followers_following_twitter_consumer_key']
    consumer_secret = data['who_are_the_followers_following_twitter_consumer_secret']

    token_key = data['who_are_the_followers_following_twitter_token_key']
    token_secret = data['who_are_the_followers_following_twitter_token_secret']
    
    print("consumer_key = {0}\nconsumer_secret={1}\ntoken_key={2}\ntoken_secret={3}".format(consumer_key, consumer_secret, token_key, token_secret))

    twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)

    line_number = 0
    if os.path.isfile(line_number_file):
        line_number = int(open(line_number_file).read())

    list_index = 0
    if os.path.isfile(list_index_file):
        list_index = int(open(list_index_file).read())

    parser = FollowerParser(line_number, followers_file)
    
    for i in range(list_index, list_index + 15):
        if i > 200:
            with open(line_number_file, 'w') as f:
                updated_line_number = line_number + 1
                f.write("{}".format(updated_line_number))


            with open(list_index_file, 'w') as f:
                updated_list_index = 0 
                f.write("{}".format(updated_list_index))

            sys.exit()

        follower = parser.get_follower(i)
        if not follower.is_protected():
            following_dict = twitter.get_friends(follower.screen_name())
            following_dict[u"follower"] = follower.screen_name()
            
            print following_dict

            with open(who_followers_follow_file, 'a') as f:
                f.write("{}\n".format(json.dumps(following_dict)))

    with open(list_index_file, 'w') as f:
        updated_list_index = list_index + 15
        f.write("{}".format(updated_list_index))
