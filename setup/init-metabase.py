from curses import meta
import requests

from os import environ
from time import sleep


class Metabase:
    host: str = environ.get("METABASE_HOST")
    port: int = environ.get("METABASE_PORT")
    email: str = environ.get("METABASE_EMAIL")
    password: str = environ.get("METABASE_PASSWORD")
    lang: str = 'en'

    @classmethod
    @property
    def base_url(cls) -> str:
        return f'http://{cls.host}:{cls.port}/api'

    @classmethod
    @property
    def user(cls) -> dict:
        user = cls.email.split('@')[0]
        return {
            'first_name': user,
            'last_name': user,
            'email': cls.email,
            'password': cls.password,
            'password_confirm': cls.password,
            'site_name': cls.host
        }

    @classmethod
    @property
    def prefs(cls) -> dict:
        return {
            'allow_tracking': False,
            'site_name': cls.host,
            'site_locale': cls.lang
        }

    @classmethod
    @property
    def database(cls) -> dict:
        return {
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
    timemout = 10

    url = f'{metabase.base_url}/session/properties'
    while retries > 0:

        try:
            response = requests.get(url, timeout=timemout)
            return response.json()['setup-token']

        except (requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout):
            sleep(wait_time)
            retries -= 1

    raise Exception('setup went wrong')


def setup(token:str, metabase=Metabase) -> str:
    response = requests.post(
        f'{metabase.base_url}/setup',
        json={
            'database': metabase.database,
            'invite': None,
            'token': token,
            'user': metabase.user,
            'prefs': metabase.prefs
        }
    )
    return response.json()['id']


if __name__ == '__main__':
    
    token = get_setup_token()
    setup(token)

