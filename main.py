from sender import Sender
from config import API_TOKEN, API_CHAT_ID


if __name__ == '__main__':
	m = Sender(API_TOKEN, API_CHAT_ID)
	m.send_message("Olá, eu sou um bot do Telegram")
