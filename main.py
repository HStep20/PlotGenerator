from generators import generate, setup
import tweepy
from tokens import *

auth = tweepy.OAuthHandler(keys2["consumerKey"], keys2["consumerSecretKey"])
auth.set_access_token(keys2["accessToken"], keys2["accessTokenSecret"])

api = tweepy.API(auth)

setup()
prompt = generate()
api.update_status(prompt)
