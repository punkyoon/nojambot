import sys
import time
import random
import tweepy

from conf import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

f = open('no-jam-gag.txt', 'r')
items = f.readlines()
f.close()

while True:
    item = random.choice(items)
    try:
        api.update_status(item)
    except tweepy.error.TweepError:
        continue
    print('Uploaded message : ' + item)
    time.sleep(MINUTES*60)  # Tweet every 'MINUTES' minutes.
