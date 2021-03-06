# -*- coding: UTF-8 -*-

from time import sleep
import multiprocessing
from twitter_client import TwitterAPI
from pi_client import PersonalityInsightsAPI
from follower_parser import FollowerParser
from personality_insights_profile import PersonalityInsightsProfile
import json
import os.path
import csv
import io
import sys
from unicode_csv import *
from datetime import datetime

twitter_handle = sys.argv[-1]
line_number_file = "{0}/{1}_line_number.txt".format(twitter_handle, twitter_handle)
list_index_file = "{0}/{1}_list_index.txt".format(twitter_handle, twitter_handle)
followers_file = "{0}/{1}_followers.json".format(twitter_handle, twitter_handle)
csv_file = "{0}/{1}_results.csv".format(twitter_handle, twitter_handle)
secrets_file = "secrets/{0}_secrets.json".format(twitter_handle)

def assemble_profile_from_tweets(tweets):
    formatted_tweets = []
    ct = 0
    for tweet in tweets:
        try:
            formatted_tweets.append({
                "content": tweet['text'],
                "contenttype": "text/plain",
                "created": int(datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y').strftime('%s')) * 1000,
                "id":tweet['id_str'],
                "language": "en",
                "sourceid": "Twitter API",
                "userid": tweet['user']['id_str']
            })
        except Exception:
            pass
    return {"contentItems": formatted_tweets}


def grab_tweets_and_run_through_pi():
    with open(secrets_file) as data_file:
        data = json.load(data_file)

        consumer_key = data['grabbing_user_tweets_twitter_consumer_key']
        consumer_secret = data['grabbing_user_tweets_twitter_consumer_secret']

        token_key = data['grabbing_user_tweets_twitter_token_key']
        token_secret = data['grabbing_user_tweets_twitter_token_secret']

        twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)

        pi_username = data['pi_username']
        pi_password = data['pi_password']

        pi = PersonalityInsightsAPI(pi_username, pi_password)

        line_number = 0
        if os.path.isfile(line_number_file):
            line_number = int(open(line_number_file).read())

        list_index = 0
        if os.path.isfile(list_index_file):
            list_index = int(open(list_index_file).read())


        # go through each user
        # save row at which you are at
        # save index of list that you are at
        # stop after 100 requests
        parser = FollowerParser(line_number, followers_file)

        with io.open(csv_file, 'ab') as csv_data:
            writer = UnicodeWriter(csv_data)

            for i in range(list_index, list_index + 100):
                follower = parser.get_follower(i)

                tweets =  twitter.get_user_timeline(follower.screen_name())
                profile = assemble_profile_from_tweets(tweets)
                try:
                    pi_profile = PersonalityInsightsProfile(pi.get_profile(profile))
                    writer.writerow([
                        follower.name(),
                        follower.screen_name(),
                        follower.location(),
                        follower.followers_count(),
                        follower.friends_count(),
                        follower.statuses_count(),
                        pi_profile.adventurousness().percentage(),
                        pi_profile.artistic_interests().percentage(),
                        pi_profile.emotionality().percentage(),
                        pi_profile.imagination().percentage(),
                        pi_profile.intellect().percentage(),
                        pi_profile.liberalism().percentage(),
                        pi_profile.conscientiousness().percentage(),
                        pi_profile.achievement_striving().percentage(),
                        pi_profile.cautiousness().percentage(),
                        pi_profile.dutifulness().percentage(),
                        pi_profile.orderliness().percentage(),
                        pi_profile.self_discipline().percentage(),
                        pi_profile.self_efficacy().percentage(),
                        pi_profile.extraversion().percentage(),
                        pi_profile.activity_level().percentage(),
                        pi_profile.assertiveness().percentage(),
                        pi_profile.cheerfulness().percentage(),
                        pi_profile.excitement_seeking().percentage(),
                        pi_profile.friendliness().percentage(),
                        pi_profile.gregariousness().percentage(),
                        pi_profile.agreeableness().percentage(),
                        pi_profile.altruism().percentage(),
                        pi_profile.cooperation().percentage(),
                        pi_profile.modesty().percentage(),
                        pi_profile.morality().percentage(),
                        pi_profile.sympathy().percentage(),
                        pi_profile.trust().percentage(),
                        pi_profile.neuroticism().percentage(),
                        pi_profile.anger().percentage(),
                        pi_profile.anxiety().percentage(),
                        pi_profile.depression().percentage(),
                        pi_profile.immoderation().percentage(),
                        pi_profile.self_consciousness().percentage(),
                        pi_profile.vulnerability().percentage(),
                        pi_profile.challenge().percentage(),
                        pi_profile.closeness().percentage(),
                        pi_profile.curiousity().percentage(),
                        pi_profile.excitement().percentage(),
                        pi_profile.harmony().percentage(),
                        pi_profile.ideal().percentage(),
                        pi_profile.liberty().percentage(),
                        pi_profile.love().percentage(),
                        pi_profile.practicality().percentage(),
                        pi_profile.self_expression().percentage(),
                        pi_profile.stability().percentage(),
                        pi_profile.structure().percentage(),
                        pi_profile.conservation().percentage(),
                        pi_profile.openness_to_change().percentage(),
                        pi_profile.hedonism().percentage(),
                        pi_profile.self_enhancement().percentage(),
                        pi_profile.self_transcendence().percentage(),
                        pi_profile.sunday().percentage(),
                        pi_profile.monday().percentage(),
                        pi_profile.tuesday().percentage(),
                        pi_profile.wednesday().percentage(),
                        pi_profile.thursday().percentage(),
                        pi_profile.friday().percentage(),
                        pi_profile.saturday().percentage(),
                        pi_profile.friday().percentage(),
                        pi_profile.midnight().percentage(),
                        pi_profile.one_am().percentage(),
                        pi_profile.two_am().percentage(),
                        pi_profile.three_am().percentage(),
                        pi_profile.four_am().percentage(),
                        pi_profile.five_am().percentage(),
                        pi_profile.six_am().percentage(),
                        pi_profile.seven_am().percentage(),
                        pi_profile.eight_am().percentage(),
                        pi_profile.nine_am().percentage(),
                        pi_profile.ten_am().percentage(),
                        pi_profile.eleven_am().percentage(),
                        pi_profile.noon().percentage(),
                        pi_profile.one_pm().percentage(),
                        pi_profile.two_pm().percentage(),
                        pi_profile.three_pm().percentage(),
                        pi_profile.four_pm().percentage(),
                        pi_profile.five_pm().percentage(),
                        pi_profile.six_pm().percentage(),
                        pi_profile.seven_pm().percentage(),
                        pi_profile.eight_pm().percentage(),
                        pi_profile.nine_pm().percentage(),
                        pi_profile.ten_pm().percentage(),
                        pi_profile.eleven_pm().percentage()
                    ])
                except Exception:
                    pass

        if list_index == 100:
            with open(line_number_file, 'w') as f:
                updated_line_number = line_number + 1
                f.write("{}".format(updated_line_number))

        with open(list_index_file, 'w') as f:
            updated_list_index = (list_index + 100) % 200
            f.write("{}".format(updated_list_index))


# timeout
p = multiprocessing.Process(target=grab_tweets_and_run_through_pi)
p.start()

p.join(210)

if p.is_alive():
    p.terminate()
    p.join()
    raise Exception("ran too long")
