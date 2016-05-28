# -*- coding: UTF-8 -*-

import json
from personality import Personality

class PersonalityInsightsProfile:
    def __init__(self, profile):
        self.profile = json.loads(profile)

    def tree(self):
        return self.profile['tree']

    def personality(self):
        return self.tree()['children'][0]

    def needs(self):
        return self.tree()['children'][1]

    def values(self):
        return self.tree()['children'][2]

    def social_behavior(self):
        return self.tree()['children'][3]

    def openness(self):
        return Personality(self.personality()['children'][0]['children'][0])

    def adventurousness(self):
        return Personality(self.openness().children()[0])

    def artistic_interests(self):
        return Personality(self.openness().children()[1])
    
    def emotionality(self):
        return Personality(self.openness().children()[2])

    def imagination(self):
        return Personality(self.openness().children()[3])

    def intellect(self):
        return Personality(self.openness().children()[4])

    def liberalism(self):
        return Personality(self.openness().children()[5])

    def conscientiousness(self):
        return Personality(self.personality()['children'][0]['children'][1])

    def achievement_striving(self):
        return Personality(self.conscientiousness().children()[0])

    def cautiousness(self):
        return Personality(self.conscientiousness().children()[1])

    def dutifulness(self):
        return Personality(self.conscientiousness().children()[2])

    def orderliness(self):
        return Personality(self.conscientiousness().children()[3])

    def self_discipline(self):
        return Personality(self.conscientiousness().children()[4])

    def self_efficacy(self):
        return Personality(self.conscientiousness().children()[5])

    def extraversion(self):
        return Personality(self.personality()['children'][0]['children'][2])

    def activity_level(self):
        return Personality(self.extraversion().children()[0])

    def assertiveness(self):
        return Personality(self.extraversion().children()[1])

    def cheerfulness(self):
        return Personality(self.extraversion().children()[2])

    def excitement_seeking(self):
        return Personality(self.extraversion().children()[3])

    def friendliness(self):
        return Personality(self.extraversion().children()[4])

    def gregariousness(self):
        return Personality(self.extraversion().children()[5])

    def agreeableness(self):
        return Personality(self.personality()['children'][0]['children'][3])

    def altruism(self):
        return Personality(self.agreeableness().children()[0])

    def cooperation(self):
        return Personality(self.agreeableness().children()[1])

    def gregariousness(self):
        return Personality(self.agreeableness().children()[2])

    def gregariousness(self):
        return Personality(self.agreeableness().children()[3])

    def gregariousness(self):
        return Personality(self.agreeableness().children()[4])

    def gregariousness(self):
        return Personality(self.agreeableness().children()[5])
