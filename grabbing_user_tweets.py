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
            break
