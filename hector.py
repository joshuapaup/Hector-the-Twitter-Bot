#----------------------------------------------------------------------------------------------------
# Important imports
#----------------------------------------------------------------------------------------------------
from credentials import *
import tweepy

#----------------------------------------------------------------------------------------------------
# Respective consumer/access keys and API authorization handles
#----------------------------------------------------------------------------------------------------
CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret
ACCESS_TOKEN = access_token
ACCESS_TOKEN_SECRET =  access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#----------------------------------------------------------------------------------------------------
# Respective tests to insure Hector works
#----------------------------------------------------------------------------------------------------
tweet = 'I am a bot named Hector! Please contact @joshua_paup for questions and inquiries!'
# tweet = 'test test test'
api.update_status(status=tweet)

#----------------------------------------------------------------------------------------------------
# A for loop that automatically follows and prints new followers
#----------------------------------------------------------------------------------------------------
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print (follower.screen_name)

#----------------------------------------------------------------------------------------------------
print('Ran successful!')
