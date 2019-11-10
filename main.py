from sender import Sender
from twitter_miner import TwitterMiner
import config as cfg

ids = {
	'SUPERVIA_TWITTER': '76395804',
}


def get_supervia_status():
	keyword = 'Belford Roxo'
	last_tweet = TwitterMiner.get_last_tweet_id(ids['SUPERVIA_TWITTER'], path)
	msg_list = tm.search_for(ids['SUPERVIA_TWITTER'], last_tweet, keyword)

	for msg in msg_list:
		sender.send_message(msg)

	TwitterMiner.update_last_tweet_id(ids['SUPERVIA_TWITTER'], tm, path)


if __name__ == '__main__':
	tm = TwitterMiner(
		key=cfg.TWITTER_API_KEY, key_secret=cfg.TWITTER_API_KEY_SECRET,
		token=cfg.TWITTER_API_TOKEN, token_secret=cfg.TWITTER_API_TOKEN_SECRET
	)
	sender = Sender(cfg.TELEGRAM_API_TOKEN, cfg.TELEGRAM_API_CHAT_ID)
	path = 'last-id.log'
	get_supervia_status()
