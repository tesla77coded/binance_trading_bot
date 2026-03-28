from bot.client import BinanceClient


class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def place_market_order(self, symbol: str, side: str, quantity: float):
        response = self.client.place_futures_order(
            symbol=symbol, side=side, order_type="MARKET", quantity=quantity
        )

        return self._format_response(response)

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        response = self.client.place_futures_order(
            symbol=symbol,
            side=side,
            order_type="LIMIT",
            quantity=quantity,
            price=price,
        )

        return self._format_response(response)

    def _format_response(self, response: dict):
        print("\n[DEBUG] Raw API Response:")
        print(response)
        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A"),
        }
