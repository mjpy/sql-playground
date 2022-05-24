import requests

from os import environ
from time import sleep


class Metabase:
    host: str = environ.get("METABASE_HOST")
    port: int = environ.get("METABASE_PORT")
    email: str = environ.get("METABASE_EMAIL")
    password: str = environ.get("METABASE_PASS")
    user: str = environ.get("METABASE_EMAIL").split('@')[0]
    site_name: str = "Metabase"
    site_locale: str = 'en'

    @classmethod
    @property
    def base_url(cls):
        return f'http://{cls.host}:{cls.port}/api'


def get_setup_token():
    retries = 5
    wait_time = 10
    timemout = 10
    while retries > 0:
        try:
            response = requests.get(f'{Metabase.base_url}/session/properties', timeout=timemout)
            return response.json()['setup-token']
        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
            sleep(wait_time)
            retries -= 1
    raise Exception('setup went wrong')


def create_admin_user(token):
    data = {
        'database': None,
        'invite': None,
        'token': token,
        'user': {
            'email': Metabase.email,
            'first_name': Metabase.user,
            'last_name': Metabase.user,
            'password': Metabase.password,
            'password_confirm': Metabase.password,
            'site_name': Metabase.site_name
        },
        'prefs': {
            'allow_tracking': False,
            'site_name': Metabase.site_name,
            'site_locale': Metabase.site_locale
        }
    }
    return requests.post(
        f'{Metabase.base_url}/setup',
        json=data
    ).json()['id']


def connect_dvdrental_db(token):
    headers = {
        'X-Metabase-Session': token
    }
    data = {
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
    return requests.post(
        f'{Metabase.base_url}/database',
        json=data, headers=headers
    ).json()


if __name__ == '__main__':
    
    setup_token = get_setup_token()
    admin_token = create_admin_user(setup_token)
    connect_dvdrental_db(admin_token)

