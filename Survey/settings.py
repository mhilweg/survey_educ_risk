from os import environ

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
SECRET_KEY = environ.get('OTREE_SECRET_KEY', 'dev-secret-key')

DEBUG = False

SESSION_CONFIGS = [
    dict(name='test',

         app_sequence=[

             'Exit_Survey'
         ],

         num_demo_participants=10,

         completionlinkfull=
            'https://app.prolific.com/submissions/complete?cc=CZ5XVQY4',


         )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

ROOMS = [
    dict( name = 'Study', display_name = 'Study'),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="", use_browser_bots=False,
)

PARTICIPANT_FIELDS = [


]
SESSION_FIELDS = {
                    'Female_quotas':{}, 'Male_quotas':{} 
                 }

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True


#DATABASES = {
   # 'default': {
  #      'ENGINE': 'django.db.backends.postgresql',
   #     'NAME': 'otree_db',           # The name of your PostgreSQL database
   #     'USER': 'otree_user',          # The username you created
   #     'PASSWORD': 'DB_PASSWORD_APPLY',   # The password for the user
    #    'HOST': 'localhost',           # Localhost for local testing
    #    'PORT': '5432',                # Default PostgreSQL port
    #}
#}