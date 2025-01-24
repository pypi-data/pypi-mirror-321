import os

from quant.application import app_factory
from quant.application.app import AppService
from quant.application.app_factory import Config


class DataSync:
    app = None

    @staticmethod
    def run():
        DataSync.__get_app().update_tickers_data()

    @staticmethod
    def run_one(symbol: str):
        DataSync.__get_app().update_ticker_data(symbol=symbol)

    @classmethod
    def __get_app(cls) -> AppService:
        if cls.app is None:
            database_url = os.environ['DATABASE_URL']
            config = Config(
                sql_alchemy_url=database_url,
            )

            cls.app = app_factory.AppFactory.init_app(config)
        return cls.app
