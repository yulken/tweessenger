import requests


class Sender:

	def __init__(self, token, chat_id):
		self.token = token
		self.chat_id = chat_id

	def send_message(self, message):
		url = f'https://api.telegram.org/bot{self.token}/sendMessage'
		data = {
			'chat_id': self.chat_id,
			'text': message,
			'parse_mode': 'html'
		}
		try:
			r = requests.get(url=url, params=data)
			if r.status_code == 400:
				raise self.APIErrorException()

		except self.APIErrorException:
			print(f"An error has ocurred: {r.status_code}")
			print(r.text)

		except requests.exceptions.ConnectionError:
			print("404 - Page Not Found")

	class APIErrorException(Exception):
		pass
