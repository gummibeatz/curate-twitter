# -*- coding: UTF-8 -*-

import json

class TwitterFollower:
    def __init__(self, follower_dict):
        self.follower_dict = follower_dict

    def name(self):
        return self.follower_dict['name']

    def screen_name(self):
        return self.follower_dict['screen_name']

    def location(self):
        return self.follower_dict['location'] or "NONE"

    def followers_count(self):
        return str(self.follower_dict['followers_count'])

    def friends_count(self):
        return str(self.follower_dict['friends_count'])

    def statuses_count(self):
        return str(self.follower_dict['statuses_count'])

    def is_protected(self):
        return self.follower_dict['protected']
