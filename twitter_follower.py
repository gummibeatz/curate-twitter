# -*- coding: UTF-8 -*-

import json

class TwitterFollower:
    def __init__(self, follower_dict):
        self.follower_dict = follower_dict

    def name(self):
        return self.follower_dict['name']
