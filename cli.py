import argparse
from bot.orders import OrderService
from bot.validators import validate_order_input


def parse_args():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument(
        "--side", required=True, choices=["BUY", "SELL"], help="Order side"
    )
    parser.add_argument(
        "--type", required=True, choices=["MARKET", "LIMIT"], help="Order type"
    )
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    return parser.parse_args()


def main():
    args = parse_args()

    print("\n=== Order Request Summary ===")
    print(vars(args))

    try:
        validate_order_input(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
    except ValueError as e:
        print(f"\n❌ Validation Error: {str(e)}")
        return

    service = OrderService()
    try:
        if args.type == "MARKET":
            result = service.place_market_order(
                symbol=args.symbol, side=args.side, quantity=args.quantity
            )

        elif args.type == "LIMIT":
            if args.price is None:
                raise ValueError("Price is required for LIMIT orders")

            result = service.place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price,
            )

        print("\n=== Order Response ===")
        for key, value in result.items():
            print(f"{key}: {value}")

        if result.get("orderId"):
            print("\n✅ Order placed successfully!")

            if result.get("status") != "FILLED":
                print(
                    "ℹ️ Order is not filled yet (status: {})".format(
                        result.get("status")
                    )
                )
        else:
            print("\n❌ Order failed!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
