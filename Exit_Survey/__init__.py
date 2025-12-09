from otree.api import *
import random


doc = '''
Third app - Exit survey.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Exit_Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
     
    
      

    



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer): 

    Education = models.IntegerField(
        choices=[
            [1, 'GCSEs/O-Levels or equivalent'],
            [2, 'A-Levels or equivalent'],
            [3, 'Undergraduate degree or equivalent'],
            [4, 'Postgraduate degree or equivalent'],
            [5, 'PhD']
        ], widget=widgets.RadioSelect)

    Risk = models.IntegerField(
        choices=[(i, str(i)) for i in range(11)],
        widget=widgets.RadioSelectHorizontal,
        label="Please select your risk level (0–10):"
    )








class Survey_Final(Page):
    form_model = 'player'
    form_fields = [
        'Risk',
        'Education'
    ]




class Redirect(Page):
    @staticmethod
    def js_vars(player):
        return dict(
            completionlinkfull=
            player.subsession.session.config['completionlinkfull']
        )



    
        
page_sequence = [
    Survey_Final,
    Redirect
    ]
