# -*- coding: UTF-8 -*-

from tweet import Tweet 
import json
import os.path
import sys

query = sys.argv[-1]
tweets_filename = "twitter_queries/{0}.json".format(query)
tweets_csvs_filename = "twitter_queries_csvs/{0}.json".format(query)

with io.open(tweets_csvs_filename, 'ab') as csv_data:
    writer = UnicodeWriter(csv_data)

    with open(tweets_filename) as tweets_file:
        for tweet_data in tweets_file:
            tweet = Tweet(json.loads(tweet_data))
            writer.writerow([
                tweet.text,
                str(tweet.id),
                str(tweet.favorite_count),
                str(','.join(tweet.user_screen_name_mentions)),
                ','.join(tweet.user_name_mentions),
                ','.join(tweet.hashtags),
                ','.join(tweet.urls),
                tweet.source,
                tweet.user.followers_count(),
                tweet.user.statuses_count(),
                tweet.user.description(),
                tweet.user.friends_count(),
                tweet.user.location(),
                tweet.user.screen_name(),
                tweet.user.lang(),
                tweet.user.name(),
                tweet.user.created_at(),
                tweet.user.time_zone(),
                str(tweet.geo),
                tweet.lang,
                tweet.created_at,
                json.dumps(tweet.place)
            ])
        
