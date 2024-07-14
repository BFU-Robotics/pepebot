import logging

import time
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID, PLANKA_API_URL
from planka import get_new_boards, get_new_projects, get_new_cards

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example logging usage
logging.info("Starting bot...")
logging.info(f"Telegram token: {TELEGRAM_TOKEN}")
logging.info(f"Chat ID: {CHAT_ID}")
logging.info(f"Planka API URL: {PLANKA_API_URL}")


print(TELEGRAM_TOKEN)
bot = Bot(token=TELEGRAM_TOKEN)


def send_message(chat_id, thread_id, text):
    bot.send_message(chat_id=chat_id, thread_id=thread_id, text=text)


def check_planka_updates():
    logging.info("Checking Planka updates...")
    new_boards = get_new_boards()
    logging.info(f"New boards: {new_boards}")
    if new_boards:
        for board in new_boards:
            message = f"New Board: {board['name']}"
            send_message(CHAT_ID, 2, message)

    new_projects = get_new_projects()
    if new_projects:
        for project in new_projects:
            message = f"New Project: {project['name']}"
            send_message(CHAT_ID, 2, message)

    new_cards = get_new_cards()
    if new_cards:
        for card in new_cards:
            message = f"New Card: {card['name']}"
            send_message(CHAT_ID, 2, message)


def check_github_updates():
    pass


def check_wiki_updates():
    pass


def main():
    while True:
        try:
            check_planka_updates()
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(60)


if __name__ == '__main__':
    main()
