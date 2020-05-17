"""
@author: pswjt
"""

import tweepy
from make_tweet import make_tweet
import schedule
import time

def job(): 
    print(make_tweet())
    
schedule.every().minute.at(":15").do(job)
schedule.every().minute.at(":45").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)
#api.update_status(tweet)