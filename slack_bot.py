import sys
import json
import random
import asyncio
import websockets

from slacker import Slacker

from conf import SLK_TOKEN, SLK_CMD_PREFIX


slack = Slacker(SLK_TOKEN)

response = slack.rtm.start()
sock_endpoint = response.body['url']


# Send message to slcak channel
def extract_message(channel, msg):
    cmd = msg.split(' ')
    if SLK_CMD_PREFIX != cmd[0]:
        return 'not command'

    if SLK_CMD_PREFIX == cmd[0] and 1 < len(cmd):
        if cmd[1] == 'help':
            slack.chat.post_message(channel,
                '> <@nojambot> 유우머',
                as_user=True
            )

        elif cmd[1] == '유우머':
            # Loading no-jam-gag
            f = open('no-jam-gag.txt', 'r')
            items = f.readlines()
            f.close()

            item = random.choice(items)

            slack.chat.post_message(channel, item, as_user=True)
        else:
            slack.chat.post_message(chaennl, '????', as_user=True)
    else:
        slack.chat.post_message(channel, '> <@nojambot> help', as_user=True)


# Get message from slack channel
async def execute_bot():
    ws = await websockets.connect(sock_endpoint)
    while True:
        msg = await ws.recv()
        ext_msg = json.loads(msg)

        try:
            if ext_msg['type'] == 'message':
                extract_message(ext_msg['channel'], ext_msg['text'])
        except:
            print('error')


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(execute_bot())
asyncio.get_event_loop().run_forever()
