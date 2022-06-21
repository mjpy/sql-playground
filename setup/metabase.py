from os import environ

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

