# -*- coding: UTF-8 -*-

import oauth2
import json
import urllib

class TwitterAPI:
    BASE_URL = 'https://api.twitter.com/1.1/'

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.client = self.get_oauth_client(consumer_key, consumer_secret, token_key, token_secret)

    def get_oauth_client(self,consumer_key, consumer_secret, token_key, token_secret):
        consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
        token = oauth2.Token(key=token_key, secret=token_secret)
        return oauth2.Client(consumer, token)

    # gets list of twitter followers for a certain screen_name
    # example response found here
    # https://dev.twitter.com/rest/reference/get/followers/list
    # default cursor of -1 gets the first page of twitter users
    def get_followers(self,screen_name, count=200, cursor = -1):
        url = self.BASE_URL + 'followers/list.json?count={0}&screen_name={1}&cursor={2}'.format(count, screen_name, cursor)
        http_method = 'GET'
        http_headers = 'Content-Type: application/json'
        resp, content = self.client.request(url, method=http_method, headers=http_headers)
        return json.loads(content)

    def get_user_timeline(self, screen_name, count=200):
        url = self.BASE_URL + 'statuses/user_timeline.json?count={0}&screen_name={1}'.format(count, screen_name)
        http_method = 'GET'
        http_headers = 'Content-Type: application/json'
        resp, content = self.client.request(url, method=http_method, headers=http_headers)
        return json.loads(content)

    def get_friends(self, screen_name):
        url = self.BASE_URL + 'friends/ids.json?screen_name={0}'.format(screen_name)
        http_method = 'GET'
        http_headers = 'Content-Type: application/json'
        resp, content = self.client.request(url, method=http_method, headers=http_headers)
        return json.loads(content)

    def search(self, query, count=100, result_type="recent"):
        encoded_query = urllib.quote_plus(query)
        url = self.BASE_URL + 'search/tweets.json?count={0}&result_type={1}&q={2}'.format(count, result_type, encoded_query)
        http_method = 'GET'
        http_headers = 'Content-Type: application/json'
        resp, content = self.client.request(url, method=http_method, headers=http_headers)
        return json.loads(content)
