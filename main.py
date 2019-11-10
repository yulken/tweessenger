from sender import Sender
from config import TELEGRAM_API_TOKEN, TELEGRAM_API_CHAT_ID


if __name__ == '__main__':
	m = Sender(TELEGRAM_API_TOKEN, TELEGRAM_API_CHAT_ID)
	m.send_message("Olá, eu sou um bot do Telegram")
