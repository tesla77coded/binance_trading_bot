import argparse


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

    print("Received order request:")
    print(vars(args))


if __name__ == "__main__":
    main()
