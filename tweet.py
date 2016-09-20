import json
from twitter_follower import TwitterFollower

class Tweet:
    def __init__(self, tweet_dict):
        self.tweet_dict = tweet_dict
        self.user = TwitterFollower(tweet_dict['user'])

    @property
    def text(self):
        return self.tweet_dict['text']

    @property
    def id(self):
        return self.tweet_dict['id']

    @property
    def favorite_count(self):
        return self.tweet_dict['favorite_count']

    @property
    def entities(self):
        return self.tweet_dict['entities']

    @property
    def user_mentions(self):
        return self.entities['user_mentions']

    @property
    def user_screen_name_mentions(self):
        return [u['screen_name'] for u in self.user_mentions]

    @property
    def user_name_mentions(self):
        return [u['name'] for u in self.user_mentions]

    @property
    def hashtags(self):
        return [h['text'] for h in self.entities['hashtags']]

    @property
    def urls(self):
        return [h['url'] for h in self.entities['urls']]

    @property
    def source(self):
        return self.tweet_dict['source'] or "NONE"

    @property 
    def geo(self):
        return self.tweet_dict['geo'] or "NONE"

    @property 
    def lang(self):
        return self.tweet_dict['lang'] or "NONE"

    @property 
    def created_at(self):
        return self.tweet_dict['created_at'] or "NONE"

    @property 
    def place(self):
        return self.tweet_dict['place'] or "NONE"
