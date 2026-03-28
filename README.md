# Trading Bot – Binance Futures Testnet

## 📌 Overview

This project is a simplified trading bot built in Python that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders via a command-line interface (CLI) with proper validation, logging, and error handling.

The application is designed with a clean, modular structure separating API interaction, business logic, validation, and CLI layers.

---

## 🚀 Features

- Place **MARKET** and **LIMIT** orders
- Supports both **BUY** and **SELL**
- CLI-based input using `argparse`
- Input validation before API execution
- Structured logging of:
  - API requests
  - API responses
  - Errors

- Clear and readable CLI output
- Modular and reusable code structure

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── logs/                  # Log files
├── cli.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd trading_bot
```

---

### 2. Create virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

### 5. Binance Testnet Setup

Use the Binance Futures Testnet:

- URL: https://testnet.binancefuture.com
- Generate API keys from the testnet dashboard
- Add test funds using the **Faucet** inside the trading UI

---

## 🧪 How to Run

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 30000
```

---

## 📤 Sample Output

```
=== Order Request Summary ===
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}

=== Order Response ===
orderId: 12345678
status: FILLED
executedQty: 0.002
avgPrice: 65000.00

✅ Order placed successfully!
```

---

## 📝 Logging

Logs are stored in:

```
logs/trading_bot.log
```

Logged details include:

- CLI request inputs
- API request parameters
- API responses
- Errors and exceptions

---

## ⚠️ Assumptions & Notes

- Only supports **BTCUSDT**-like symbols in uppercase
- Basic validation is implemented (symbol, side, type, quantity, price)
- Exchange-level constraints (e.g., min notional, precision, step size) are **not pre-validated** and are handled by Binance API responses
- LIMIT orders may remain in `NEW` status if market price is not reached
- MARKET orders are used to verify execution (`FILLED` status)

---

## ❗ Error Handling

The application handles:

- Invalid user input (validation layer)
- API errors (e.g., insufficient margin, invalid quantity)
- Network / unexpected failures

All errors are:

- Displayed clearly in CLI
- Logged to file

---

## 📦 Dependencies

- python-binance
- python-dotenv

---

## ✅ Example Logs (Required)

The `logs/` directory contains:

- MARKET order execution logs
- LIMIT order execution logs

---

## 🧠 Design Highlights

- Separation of concerns (CLI, validation, service, API client)
- Reusable client wrapper
- Centralized validation logic
- Structured logging for observability
- Clean and minimal CLI UX

---

## 📬 Conclusion

This project demonstrates:

- API integration
- Error handling
- Input validation
- Logging and observability
- Clean backend-oriented design

---
