import requests


class Sender:

	def __init__(self, token, chat_id):
		self.token = token
		self.chat_id = chat_id

	def send_message(self, message):
		url = f'https://api.telegram.org/bot{self.token}/sendMessage'
		data = {
			'chat_id': self.chat_id,
			'text': message
		}
		r = requests.get(url=url, params=data)
		print(r.status_code)
