from generators import generate, setup
import tweepy, praw
from tokens import *
setup()
prompt = generate()

#Twitter
def twitterpost():
    auth = tweepy.OAuthHandler(twitterKeys2["consumerKey"], twitterKeys2["consumerSecretKey"])
    auth.set_access_token(twitterKeys2["accessToken"], twitterKeys2["accessTokenSecret"])
    api = tweepy.API(auth)
    api.update_status(prompt)

#Reddit
def redditpost():
    reddit = praw.Reddit(
        client_id=redditKeys["client_id"],
        client_secret=redditKeys["client_secret"],
        user_agent=redditKeys["user_agent"],
        username="BrainstormCentral",
        password=redditKeys["password"]
    )
    reddit.subreddit("BrainstormPrompts").submit(prompt, selftext="")

twitterpost()
redditpost()
