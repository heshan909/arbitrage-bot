import requests
import time

def get_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data = requests.get(url).json()
    return float(data['price'])

def get_coinbase_price(symbol="BTC-USD"):
    url = f"https://api.coinbase.com/v2/prices/{symbol}/spot"
    data = requests.get(url).json()
    return float(data['data']['amount'])

def find_arbitrage_opportunity():
    binance_price = get_binance_price()
    coinbase_price = get_coinbase_price()

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
        try:
            find_arbitrage_opportunity()
            time.sleep(10)  # refresh every 10 seconds
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)
