# -*- coding: UTF-8 -*-

class Personality:
    def __init__(self, profile):
        self.profile = profile

    def id(self):
        return self.profile['id']

    def name(self):
        return self.profile['name']

    def category(self):
        return self.profile['category']

    def percentage(self):
        return str(self.profile['percentage'])

    def sampling_error(self):
        return self.profile['sampling_error']

    def children(self):
        return self.profile['children']
