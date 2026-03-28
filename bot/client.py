import os
from binance.client import Client
from dotenv import load_dotenv


class BinanceClient:
    def __init__(self) -> None:
        load_dotenv()

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API keys not found.")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_future_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")

                params.update({"price": price, "timeInForce": "GTC"})

            response = self.client.futures_create_order(**params)
            return response

        except Exception as e:
            raise RuntimeError(f"Failed to place order: {str(e)}")
