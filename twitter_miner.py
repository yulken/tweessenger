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
		self.msg_list = []

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
	def update_last_tweet_id(target_id,logged_id, twitter_miner, path):
		last_tweet = twitter_miner.get_last_remote_tweet_id(target_id)
		if last_tweet != logged_id:
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

	@staticmethod
	def build_message(tweet):
		msg = f'<b>Message from {tweet["user"]["name"]}</b>:\n'
		msg += f'{tweet["full_text"]}\n'
		msg += f'https://twitter.com/user/status/{tweet["id"]}'
		return msg

	def search_for(self, keywords, tweet, tweet_type):
		for word in keywords:
			if re.search(word, tweet['full_text'], re.IGNORECASE):
				if tweet_type == 'mention':
					return tweet
				else:
					self.msg_list.append(TwitterMiner.build_message(tweet))

	def get_new_tweets(self, target_id, last_tweet_id, keywords):
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
		for tweet in tl:
			self.search_for(keywords, tweet, 'status')
			if tweet['in_reply_to_status_id'] is not None:
				mention = self.api.get_status(
					id=tweet['in_reply_to_status_id'],
					tweet_mode="extended"
				)
				if self.search_for(keywords, mention, 'mention'):
					self.msg_list.append(TwitterMiner.build_message(tweet))
		return self.msg_list

