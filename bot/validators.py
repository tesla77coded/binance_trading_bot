def validate_symbol(symbol: str):
    if not symbol or not symbol.isupper():
        raise ValueError("Symbol must be uppercase (e.g., BTCUSDT)")


def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price: float):
    if price is None or price <= 0:
        raise ValueError("Price must be provided and greater than 0 for LIMIT orders")


def validate_order_input(symbol, side, order_type, quantity, price):
    validate_symbol(symbol)
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)

    if order_type == "LIMIT":
        validate_price(price)
