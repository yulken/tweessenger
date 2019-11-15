import tweepy
import re


class TwitterMiner:
	def __init__(self, key, key_secret, token, token_secret):
		auth = tweepy.OAuthHandler(
			consumer_key=key,
			consumer_secret=key_secret
		)
		auth.set_access_token(
			key=token,
			secret=token_secret
		)
		self.api = tweepy.API(
			auth,
			parser=tweepy.parsers.JSONParser()
		)

	@staticmethod
	def get_last_tweet_id(target_id, path):
		try:
			f = open(path, 'r')
			for line in reversed(f.readlines()):
				if re.search(target_id, line):
					last_tweet = line.split(';')[1]
					return int(last_tweet)

			f.close()
		except FileNotFoundError:
			print("File not found")

	@staticmethod
	def update_last_tweet_id(target_id, twitter_miner, path):
		last_tweet = twitter_miner.get_last_remote_tweet_id(target_id)
		if last_tweet != TwitterMiner.get_last_tweet_id(target_id, path):
			f = open(path, 'a+')
			f.write(f'{target_id};{last_tweet}\n')
			f.close()

	def get_last_remote_tweet_id(self, target_id):
		tl = self.api.user_timeline(
			id=target_id,
			tweet_mode="extended",
			count=1
		)
		return tl[0]['id']

	def search_for(self, target_id, last_tweet_id, keywords):
		if last_tweet_id is None:
			tl = self.api.user_timeline(
				id=target_id,
				tweet_mode="extended"
			)
		else:
			tl = self.api.user_timeline(
				id=target_id,
				tweet_mode="extended",
				since_id=last_tweet_id
			)
		msg_list = []
		for tweet in tl:
			msg = ''
			for word in keywords:
				if re.search(word, tweet['full_text'], re.IGNORECASE):
					msg += f'<b>Message from {tweet["user"]["name"]}</b>:\n'
					msg += f'{tweet["full_text"]}\n'
					msg += f'https://twitter.com/user/status/{tweet["id"]}'
					msg_list.append(msg)
		return msg_list

