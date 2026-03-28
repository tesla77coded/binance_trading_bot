import time
from bot.client import BinanceClient


class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def place_market_order(self, symbol: str, side: str, quantity: float):
        response = self.client.place_futures_order(
            symbol=symbol, side=side, order_type="MARKET", quantity=quantity
        )

        time.sleep(1)

        updated = self.client.client.futures_get_order(
            symbol=symbol, orderId=response["orderId"]
        )

        return self._format_response(updated)

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        response = self.client.place_futures_order(
            symbol=symbol,
            side=side,
            order_type="LIMIT",
            quantity=quantity,
            price=price,
        )

        time.sleep(1)

        updated = self.client.client.futures_get_order(
            symbol=symbol, orderId=response["orderId"]
        )

        return self._format_response(updated)

    def _format_response(self, response: dict):
        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A"),
        }
