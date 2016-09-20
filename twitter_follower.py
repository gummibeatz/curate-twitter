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

    def description(self):
        return self.follower_dict['description'] or "NONE"

    def lang(self):
        return self.follower_dict['lang'] or "NONE"

    def created_at(self):
        return self.follower_dict['created_at'] or "NONE"

    def time_zone(self):
        return self.follower_dict['time_zone'] or "NONE"
