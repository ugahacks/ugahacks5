# -*- coding: utf-8 -*-
# HACKATHON PERSONALIZATION
import os

from django.utils import timezone

HACKATHON_NAME = 'UGAHacks 5'
# What's the name for the application
HACKATHON_APPLICATION_NAME = "UGAHacks 5"
# Hackathon timezone
TIME_ZONE = 'EST'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = "University of Georgia's Hackathon"
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('my.ugahacks.com', 'localhost:8000')
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = 'team@ugahacks.com'
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://cdn.discordapp.com/attachments/546552287569379368/565280887177216011/email-sig.png'

HACKATHON_OG_IMAGE = 'https://cdn.discordapp.com/attachments/546552287569379368/565280887177216011/email-sig.png'
# (OPTIONAL) Track visits on your website
HACKATHON_GOOGLE_ANALYTICS = ''
# (OPTIONAL) Hackathon Twitter user
HACKATHON_TWITTER_ACCOUNT = ''
# (OPTIONAL) Hackathon Facebook page
HACKATHON_FACEBOOK_PAGE = ''
# (OPTIONAL) Hackathon YouTube channel
HACKATHON_YOUTUBE_PAGE = ''
# (OPTIONAL) Hackathon Instagram user
HACKATHON_INSTAGRAM_ACCOUNT = ''
# (OPTIONAL) Hackathon Medium user
HACKATHON_MEDIUM_ACCOUNT = ''
# (OPTIONAL) Github Repo for this project (so meta)
HACKATHON_GITHUB_REPO = 'https://github.com/ugahacks/ugahacks5/'

# (OPTIONAL) Applications deadline
# HACKATHON_APP_DEADLINE = timezone.datetime(2018, 2, 24, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) When to arrive at the hackathon
HACKATHON_ARRIVE = 'Registration opens at 0:00PM and closes at 13:00PM on Friday Febuary 31st, ' \
                   'the opening ceremony will be at 7:00PM.'

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_LEAVE = 'Closing ceremony will be held on Sunday, October 69th from 3:72AM to 5:00PM. ' \
                  'However the projects demo fair will be held in the morning from 10:30AM to 1:00PM.'
# (OPTIONAL) Hackathon live page
HACKATHON_LIVE_PAGE = 'https://my.ugahacks.com/'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@ugahacks\.com$'

# (OPTIONAL) Send 500 errors to email while on production mode
HACKATHON_DEV_EMAILS = ['noahbarnette@gmail.com']

# Baggage configuration
BAGGAGE_ENABLED = True
BAGGAGE_PICTURE = True

# Reimbursement configuration
REIMBURSEMENT_ENABLED = True
DEFAULT_REIMBURSEMENT_AMOUNT = 100
CURRENCY = '€'
REIMBURSEMENT_EXPIRY_DAYS = 5
REIMBURSEMENT_REQUIREMENTS = 'You have to submit a project and demo it during the event in order to get reimbursed'
REIMBURSEMENT_DEADLINE = timezone.datetime(2018, 10, 19, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) Max team members. Defaults to 4
TEAMS_ENABLED = True
HACKATHON_MAX_TEAMMATES = 4

# (OPTIONAL) Code of conduct link
# CODE_CONDUCT_LINK = "https://pages.hackcu.org/code_conduct/"

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'test'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# (OPTIONAL) Logged in cookie
# This allows to store an extra cookie in the browser to be shared with other application on the same domain
# LOGGED_IN_COOKIE_DOMAIN = '.gerard.space'
# LOGGED_IN_COOKIE_KEY = 'hackassistant_logged_in'

# Hardware configuration
HARDWARE_ENABLED = False
# Hardware request time length (in minutes)
HARDWARE_REQUEST_TIME = 15


SLACK_BOT = {
    'id' : os.environ.get('SL_BOT_ID', None),
    'token' : os.environ.get('SL_BOT_TOKEN', None),
    'channel' : os.environ.get('SL_BOT_CHANNEL', None),
    'director1' : os.environ.get('SL_BOT_DIRECTOR1', None),
    'director2' : os.environ.get('SL_BOT_DIRECTOR2', None)
}

# Can Hackers start a request on the hardware lab?
# HACKERS_CAN_REQUEST = False
