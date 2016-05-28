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

    def modesty(self):
        return Personality(self.agreeableness().children()[2])

    def morality(self):
        return Personality(self.agreeableness().children()[3])

    def sympathy(self):
        return Personality(self.agreeableness().children()[4])

    def trust(self):
        return Personality(self.agreeableness().children()[5])

    def neuroticism(self):
        return Personality(self.personality()['children'][0]['children'][4])

    def anger(self):
        return Personality(self.agreeableness().children()[0])

    def anxiety(self):
        return Personality(self.agreeableness().children()[1])

    def depression(self):
        return Personality(self.agreeableness().children()[2])

    def immoderation(self):
        return Personality(self.agreeableness().children()[3])

    def self_consciousness(self):
        return Personality(self.agreeableness().children()[4])

    def vulnerability(self):
        return Personality(self.agreeableness().children()[5])
    
    def challenge(self):
        return Personality(self.needs()['children'][0]['children'][0])

    def closeness(self):
        return Personality(self.needs()['children'][0]['children'][1])

    def curiousity(self):
        return Personality(self.needs()['children'][0]['children'][2])

    def excitement(self):
        return Personality(self.needs()['children'][0]['children'][3])

    def harmony(self):
        return Personality(self.needs()['children'][0]['children'][4])

    def ideal(self):
        return Personality(self.needs()['children'][0]['children'][5])

    def liberty(self):
        return Personality(self.needs()['children'][0]['children'][6])

    def love(self):
        return Personality(self.needs()['children'][0]['children'][7])

    def practicality(self):
        return Personality(self.needs()['children'][0]['children'][8])

    def self_expression(self):
        return Personality(self.needs()['children'][0]['children'][9])

    def stability(self):
        return Personality(self.needs()['children'][0]['children'][10])

    def structure(self):
        return Personality(self.needs()['children'][0]['children'][11])

    def conservation(self):
        return Personality(self.values()['children'][0]['children'][0])

    def openness_to_change(self):
        return Personality(self.values()['children'][0]['children'][1])

    def hedonism(self):
        return Personality(self.values()['children'][0]['children'][2])

    def self_enhancement(self):
        return Personality(self.values()['children'][0]['children'][3])

    def self_transcendence(self):
        return Personality(self.values()['children'][0]['children'][4])

    def days(self):
        return Personality(self.social_behavior()['children'][0]['children'][0])

    def sunday(self):
        return Personality(self.days().children()[0])

    def monday(self):
        return Personality(self.days().children()[1])

    def tuesday(self):
        return Personality(self.days().children()[2])

    def wednesday(self):
        return Personality(self.days().children()[3])

    def thursday(self):
        return Personality(self.days().children()[4])

    def friday(self):
        return Personality(self.days().children()[5])

    def saturday(self):
        return Personality(self.days().children()[6])

    def hours(self):
        return Personality(self.social_behavior()['children'][0]['children'][1])
    
    def midnight(self):
        return Personality(self.hours().children()[0])

    def one_am(self):
        return Personality(self.hours().children()[1])

    def two_am(self):
        return Personality(self.hours().children()[2])

    def three_am(self):
        return Personality(self.hours().children()[3])

    def four_am(self):
        return Personality(self.hours().children()[4])

    def five_am(self):
        return Personality(self.hours().children()[5])

    def six_am(self):
        return Personality(self.hours().children()[6])

    def seven_am(self):
        return Personality(self.hours().children()[7])

    def eight_am(self):
        return Personality(self.hours().children()[8])

    def nine_am(self):
        return Personality(self.hours().children()[9])

    def ten_am(self):
        return Personality(self.hours().children()[10])

    def eleven_am(self):
        return Personality(self.hours().children()[11])

    def noon(self):
        return Personality(self.hours().children()[12])

    def one_pm(self):
        return Personality(self.hours().children()[13])

    def two_pm(self):
        return Personality(self.hours().children()[14])

    def three_pm(self):
        return Personality(self.hours().children()[15])

    def four_pm(self):
        return Personality(self.hours().children()[16])

    def five_pm(self):
        return Personality(self.hours().children()[17])

    def six_pm(self):
        return Personality(self.hours().children()[18])

    def seven_pm(self):
        return Personality(self.hours().children()[19])

    def eight_pm(self):
        return Personality(self.hours().children()[20])

    def nine_pm(self):
        return Personality(self.hours().children()[21])

    def ten_pm(self):
        return Personality(self.hours().children()[22])

    def eleven_pm(self):
        return Personality(self.hours().children()[23])
