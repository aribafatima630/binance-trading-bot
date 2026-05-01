# 📈 Binance Futures Trading Bot (Testnet)

## 🚀 Overview

This project is a **CLI-based Python trading bot** that interacts with the **Binance Futures Testnet (USDT-M)** to place orders.

It supports:

* ✅ MARKET and LIMIT orders
* ✅ BUY and SELL sides
* ✅ Input validation and error handling
* ✅ Structured logging of API requests and responses

The application is designed with a **clean, modular architecture**, making it easy to extend and maintain.

---

## 🛠️ Tech Stack

* Python 3.x
* `python-binance`
* `Typer` (CLI)
* `Rich` (formatted output)
* `Tenacity` (retry handling)
* Logging (JSON format)

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── logs/
│   └── trading.log        # API request/response logs
│
├── cli.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/aribafatima630/binance-trading-bot.git
cd trading_bot
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
```

👉 Generate keys from:
https://testnet.binancefuture.com

---

## ▶️ How to Run

```
python cli.py
```

---

## 🧪 Example Run

```
Enter symbol (e.g. BTCUSDT): BTCUSDT
Side (BUY/SELL): BUY
Order Type (MARKET/LIMIT): MARKET
Quantity (e.g. 0.001): 0.001
```

### ✔ Output

```
📤 Order Request Summary:
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.001

✅ ORDER SUCCESS

📊 Order Response Details:
Order ID: 123456789
Status: NEW
Executed Quantity: 0.0000
Average Price: 0.00
```

---

## 📊 Logging

All API interactions are logged in:

```
logs/trading.log
```

Includes:

* Request payload
* API response
* Errors (if any)

👉 Log format is structured JSON for readability and debugging.

---

## ⚠️ Assumptions & Notes

* Uses **Binance Futures Testnet**, not real trading environment
* LIMIT orders may remain in `NEW` status (expected behavior on testnet)
* Price for LIMIT orders is **auto-adjusted** to:

  * satisfy minimum notional (≥ 50 USDT)
  * match Binance tick size rules
* Retry logic is implemented for transient failures

---

## ✅ Features Implemented (as per requirements)

* ✔ MARKET and LIMIT order placement
* ✔ BUY and SELL support
* ✔ CLI input using Typer
* ✔ Input validation
* ✔ Structured logging
* ✔ Exception handling (API + input + network)
* ✔ Clean modular code structure

---

## ⭐ Bonus Enhancements

* 🔥 Smart LIMIT order handling (auto price adjustment)
* 🔥 Clean CLI UX with formatted output
* 🔥 JSON logging for production-like debugging

---

## 🏁 Conclusion

This project demonstrates:

* Practical API integration
* Clean code architecture
* Handling of real-world trading constraints
* Robust error handling and logging

---

## 👤 Author

Ariba Fatima
(BCA Student | Aspiring Backend & GenAI Engineer)
