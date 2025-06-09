import requests
import time

def get_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'price' in data:
            return float(data['price'])
        else:
            print("Unexpected Binance response:", data)
            return None
    except Exception as e:
        print(f"Binance API error: {e}")
        return None

def get_coinbase_price(symbol="BTC-USD"):
    url = f"https://api.coinbase.com/v2/prices/{symbol}/spot"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'amount' in data['data']:
            return float(data['data']['amount'])
        else:
            print("Unexpected Coinbase response:", data)
            return None
    except Exception as e:
        print(f"Coinbase API error: {e}")
        return None

def find_arbitrage_opportunity():
    binance_price = get_binance_price()
    coinbase_price = get_coinbase_price()

    if binance_price is None or coinbase_price is None:
        print("Skipping due to error.")
        return

    spread = coinbase_price - binance_price
    percentage_diff = (spread / binance_price) * 100

    print(f"Binance BTC/USDT: ${binance_price:.2f}")
    print(f"Coinbase BTC/USD: ${coinbase_price:.2f}")
    print(f"Spread: ${spread:.2f} | Diff: {percentage_diff:.2f}%")

    threshold = 0.5  # percent
    if abs(percentage_diff) > threshold:
        print("🔍 Arbitrage opportunity detected!")
    else:
        print("No significant arbitrage opportunity.")

if __name__ == "__main__":
    while True:
        find_arbitrage_opportunity()
        time.sleep(10)
