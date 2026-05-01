import typer
from rich import print
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity

app = typer.Typer(help="📈 Binance Futures Testnet Trading Bot")


@app.command()
def trade():
    """
    Place a trade on Binance Futures Testnet
    """

    # 📥 User Input
    symbol = typer.prompt("Enter symbol (e.g. BTCUSDT)").upper()
    side = typer.prompt("Side (BUY/SELL)").upper()
    order_type = typer.prompt("Order Type (MARKET/LIMIT)").upper()

    try:
        quantity = float(typer.prompt("Quantity (e.g. 0.001)"))
    except ValueError:
        print("[bold red]❌ Quantity must be a number[/bold red]")
        raise typer.Exit()

    price = None
    if order_type == "LIMIT":
        try:
            price = float(typer.prompt("Price (optional, will auto-adjust if invalid)"))
        except ValueError:
            print("[bold red]❌ Price must be a number[/bold red]")
            raise typer.Exit()

    # ✅ Validation
    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
    except Exception as e:
        print(f"[bold red]❌ Validation Error: {str(e)}[/bold red]")
        raise typer.Exit()

    # 📤 Request Summary (REQUIRED by task)
    print("\n📤 [bold]Order Request Summary:[/bold]")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Order Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price:
        print(f"Price: {price}")

    try:
        client = BinanceClient()

        order = place_order(client, symbol, side, order_type, quantity, price)

        # ✅ Success Output (REQUIRED by task)
        print("\n[bold green]✅ ORDER SUCCESS[/bold green]")

        print("\n📊 [bold]Order Response Details:[/bold]")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Quantity: {order.get('executedQty')}")
        print(f"Average Price: {order.get('avgPrice')}")

    except Exception as e:
        print(f"\n[bold red]❌ ORDER FAILED[/bold red]")
        print(f"[bold red]{str(e)}[/bold red]")


if __name__ == "__main__":
    app()