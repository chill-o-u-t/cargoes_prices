import os

from dotenv import load_dotenv
from typing import Union

import pydantic as pd

load_dotenv()


class Settings(pd.BaseSettings):
    """
    App settings.
    """
    path: str
    debug: bool = True
    echo: Union[None, bool] = None
    app_title: str = 'cargoes_rates'
    description: str = 'Calculated prices to cargoes'
    database_url: str = ''
    secret = os.getenv('SECRET')
    first_superuser_email: Union[None, pd.EmailStr] = None
    first_superuser_password: Union[None, str] = None

    class Config:
        env_file = '.env'


settings = Settings()

if settings.debug and settings.echo is None:
    settings.echo = True


DATABASE_CONFIG = {
    "connections": {"default": os.getenv('DB_CONNECTION_URL')},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.model"],
            "default_connection": "default",
        },
    },
}
