import json
import random
import logging
import asyncio
import websockets

from slacker import Slacker

from conf import TOKEN, BOT_NAME


logger = logging.getLogger('nojam_slack')


class Slack:
    def __init__(self):
        # Init slack bot config
        self.bot_name = BOT_NAME
        self.slack = Slacker(TOKEN)
        self.response = self.slack.rtm.start()
        self.endpoint = self.response.body['url']

        # Load nojam gag
        with open('no-jam-gag.txt', 'r') as nojam:
            self.items = nojam.readlines()

        # Init default msg
        self.msg = None

    def extract_message(self, channel, cmd):
        # Extract command
        cmd = cmd.split(' ')

        # Send messages to slack channel
        if self.bot_name == cmd[0] and 1 < len(cmd):
            if cmd[1] == 'help':
                self.msg = '> <@nojambot> 유우머'

            elif cmd[1] == '유우머':
                self.msg = random.choice(self.items)

            else:
                # Cannot understand
                self.msg = '????'

        elif self.bot_name == cmd[0]:
            self.msg = '> <@nojambot> help'

    def send_message(self, channel):
        if self.msg:
            self.slack.chat.post_message(channel, self.msg, as_user=True)
            logger.info('Sended message: {}'.format(self.msg))
        self.msg = None

    async def execute_bot(self):
        ws = await websockets.connect(self.endpoint)
        while True:
            cmd = await ws.recv()
            json_cmd = json.loads(cmd)

            if 'type' in json_cmd and json_cmd['type'] == 'message':
                try:
                    self.extract_message(
                        json_cmd['channel'],
                        json_cmd['text']
                    )
                    self.send_message(json_cmd['channel'])
                except Exception as e:
                    logger.error(e)
