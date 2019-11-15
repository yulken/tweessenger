from sender import Sender
from twitter_miner import TwitterMiner
import config as cfg
from datetime import datetime

ids = {
	'SUPERVIA_TWITTER': '76395804',
}


def get_time(status):
	time = datetime.now()
	print(f'{time.strftime("%Y/%m/%d_%H:%M:%S")} - {status}')


def get_supervia_status():
	keywords = [
		'Belford Roxo',
		'BelfordRoxo',
		'Japeri'

	]
	last_tweet = TwitterMiner.get_last_tweet_id(ids['SUPERVIA_TWITTER'], path)
	msg_list = tm.get_new_tweets(ids['SUPERVIA_TWITTER'], last_tweet, keywords)
	if msg_list:
		for msg in msg_list:
			sender.send_message(msg)

	TwitterMiner.update_last_tweet_id(ids['SUPERVIA_TWITTER'], tm, path)


if __name__ == '__main__':
	get_time('Starting')
	tm = TwitterMiner(
		key=cfg.TWITTER_API_KEY, key_secret=cfg.TWITTER_API_KEY_SECRET,
		token=cfg.TWITTER_API_TOKEN, token_secret=cfg.TWITTER_API_TOKEN_SECRET
	)
	sender = Sender(cfg.TELEGRAM_API_TOKEN, cfg.TELEGRAM_API_CHAT_ID)
	path = 'last-id.log'
	get_supervia_status()
	get_time('Done')

