# telegram_alert.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Telegram alert sent!")
    else:
        print("❌ Failed to send alert")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Test alert
send_telegram_alert("🚨 This is a test alert from the arbitrage bot.")

