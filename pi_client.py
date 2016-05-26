# -*- coding: UTF-8 -*-

import requests
import json

class PersonalityInsightsAPI:
    BASE_URL = 'https://gateway.watsonplatform.net/personality-insights/api/v2/'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_profile(self, profile):
        url = self.BASE_URL + 'profile'
        payload={"profile" : profile}
        resp = requests.post(url, auth=(self.username, self.password), json=payload)
        print resp.text




# example of how it has to be formatted. WHAT the fuck tho.... really? all those fields?
# but also here's an example so yay
#
p = PersonalityInsightsAPI('some_username','some_password')

profile = """{
   "contentItems": [
      {
         "content": "Wow, I liked @TheRock before , now I really SEE how special he is. The daughter story was IT for me. So great! #MasterClass",
         "contenttype": "text/plain",
         "created": 1447639154000,
         "id": "666073008692314113",
         "language": "en",
         "sourceid": "Twitter API",
         "userid": "@Oprah"
      }
    ]
    }"""

p.get_profile(profile)
