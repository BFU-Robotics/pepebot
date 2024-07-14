import logging

import requests
from config import PLANKA_API_URL


def get_new_boards():
    logging.info("Ping1")
    logging.info(f"{PLANKA_API_URL}/boards/new/")
    response = requests.get(f"{PLANKA_API_URL}/boards/new/")
    logging.info("Ping2")
    return response.json()


def get_new_projects():
    response = requests.get(f"{PLANKA_API_URL}/projects/new/")
    return response.json()


def get_new_cards():
    response = requests.get(f"{PLANKA_API_URL}/cards/new/")
    return response.json()
