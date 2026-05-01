from bot.logging_config import logger
import json

def get_market_price(client, symbol):
    ticker = client.client.futures_symbol_ticker(symbol=symbol)
    return float(ticker["price"])


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        payload = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            market_price = get_market_price(client, symbol)

            if side == "BUY":
                price = market_price * 0.95
            else:
                price = market_price * 1.05

            # Ensure notional >= 50
            if quantity * price < 60:
                quantity = round(60 / price, 3)

            # Adjust to tick size
            price = round(price, 1)

            payload["price"] = price
            payload["quantity"] = quantity
            payload["timeInForce"] = "GTC"

        logger.info("REQUEST: %s", json.dumps(payload))

        response = client.create_order(**payload)

        logger.info("RESPONSE: %s", json.dumps(response))

        return response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise