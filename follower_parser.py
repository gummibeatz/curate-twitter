# -*- coding: UTF-8 -*-

from twitter_follower import TwitterFollower
import json


class FollowerParser:
    def __init__(self, line_number, filename):
        self.line_number = line_number
        self.follower_array = self.get_follower_array(filename, line_number)

    def get_follower_array(self, filename, line_number):
        f = open(filename)
        for i, line in enumerate(f): 
            if i == self.line_number:
                f.close()
                return json.loads(line)
        f.close()
        return 0

    def get_follower(self, index):
        return TwitterFollower(self.follower_array[index])
