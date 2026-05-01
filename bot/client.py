from binance.client import Client
import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed
from binance.exceptions import BinanceAPIException

load_dotenv()

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("API keys not found in environment variables")

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True,
        )

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def create_order(self, **kwargs):
        try:
            response = self.client.futures_create_order(**kwargs)
            return response

        except BinanceAPIException as e:
            print("❌ BINANCE ERROR:", e.message)
            raise Exception(e.message)