import time
import random
import logging

import tweepy

from conf import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_SECRET,
    MINUTES
)


logger = logging.getLogger('nojam_twitter')


class Twitter:
    def __init__(self):
        # Init twitter bot config
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

        # Load nojam gag
        with open('no-jam-gag.txt', 'r') as nojam:
            self.items = nojam.readlines()

        # Init default msg
        self.msg = ''

        self.logger = logging.getLogger('nojam_twitter')
        self.logger.setLevel(logging.INFO)


    def extract_message(self):
        self.msg = random.choice(self.items)

    def send_message(self):
        try:
            self.api.update_status(self.msg)
        except Exception as e:
            self.logger.error(e)
            return

        self.logger.info('Uploaded message: {}'.format(self.msg))

    def execute_bot(self):
        while True:
            self.extract_message()
            self.send_message()
            time.sleep(MINUTES * 60)
