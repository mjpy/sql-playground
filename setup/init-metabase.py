import requests

from time import sleep
from pathlib import Path

from metabase import Metabase
from card import Card


CARDS_FOLDER = 'cards'
DB_DVDRENTAL = {
            'engine': 'postgres',
            'name': 'dvdrental',
            'details': {
                'host': 'postgres',
                'port': '5432',
                'db': 'dvdrental',
                'user': 'postgres',
                'password': 'password'
            }
        }


def get_setup_token(metabase=Metabase) -> str:
    retries = 5
    wait_time = 10
    timeout = 10

    url = f'{metabase.base_url}/session/properties'
    while retries > 0:

        try:
            response = requests.get(url, timeout=timeout)
            return response.json()['setup-token']

        except (requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout):
            sleep(wait_time)
            retries -= 1

    raise Exception('setup went wrong')


def setup(token:str, metabase=Metabase, database=DB_DVDRENTAL) -> str:
    response = requests.post(
        f'{metabase.base_url}/setup',
        json={
            'database': database,
            'invite': None,
            'token': token,
            'user': metabase.user,
            'prefs': metabase.prefs
        }
    )
    return response.json()['id']


def create_card(token:str, card:Card, metabase=Metabase) -> str:
    return requests.post(
        f'{metabase.base_url}/card',
        headers={"X-Metabase-Session": token},
        json=card.payload
    )


def create_cards(token:str, metabase=Metabase, cards_folder=CARDS_FOLDER) -> None:
    dir = Path(cards_folder)
    for filepath in dir.glob('**/*.sql'):
        card = Card.from_file(filepath)
        create_card(token, card)
    return None


def main():
    setup_token = get_setup_token()
    token = setup(setup_token)
    create_cards(token)


if __name__ == '__main__':
    main()

