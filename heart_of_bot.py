import logging
import asyncio
import argparse


logger = logging.getLogger('nojam')
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    # Use argument parser
    parser = argparse.ArgumentParser(
        description='This is a script to run nojambot'
    )
    parser.add_argument(
        'mode',
        help='Choose whether to run on Slack or Twitter',
        choices=['twitter', 'slack'],
        type=str
    )

    args = parser.parse_args()

    if args.mode == 'twitter':
        logger.info('Run on Twitter')

        from twitter_bot import Twitter

        twt = Twitter()
        try:
            twt.execute_bot()
        except KeyboardInterrupt:
            logger.info('Terminate nojambot on Twitter')

    else:
        logger.info('Run on Slack')

        from slack_bot import Slack

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        slk = Slack()
        try:
            asyncio.get_event_loop().run_until_complete(slk.execute_bot())
            asyncio.get_event_loop().run_forever()
        except KeyboardInterrupt:
            logger.info('Terminate nojambot on Slack')
