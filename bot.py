"""
@author: pswjt
"""

import tweepy
import schedule
import time
from os import environ
from make_tweet import make_tweet

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def job():
    tweet = make_tweet()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(tweet)
    
schedule.every().day.at("8:20").do(job)
schedule.every().day.at("20:20").do(job)

while True:
    schedule.run_pending()
    time.sleep(61)
    
