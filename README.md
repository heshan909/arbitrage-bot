# 🧠 Crypto Arbitrage Bot

A simple Python bot that scans for cryptocurrency arbitrage opportunities and optionally sends Telegram alerts when profitable conditions are detected.

> Repository: [github.com/heshan909/arbitrage-bot](https://github.com/heshan909/arbitrage-bot)

---

## 🚀 Features

- 📈 Realtime price fetching from crypto exchanges (e.g. Binance)
- 🔍 Identifies arbitrage opportunities between markets
- 🔔 Sends Telegram alerts (optional, via `.env` config)
- 🔗 Modular design with a separate alert handler

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
If requirements.txt doesn’t exist yet, install manually:

bash
Copy
Edit
pip install requests python-dotenv
⚙️ Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/heshan909/arbitrage-bot.git
cd arbitrage-bot
2. Create a .env file
Create a file named .env in the root of the project and add your Telegram bot credentials:

ini
Copy
Edit
TELEGRAM_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
⚠️ Never share this file or commit it to GitHub.

▶️ Usage
Run the main bot:

bash
Copy
Edit
python arbitrage_bot.py
To test Telegram alerts independently:

bash
Copy
Edit
python telegram_alert.py
🔐 Security
.env is excluded via .gitignore

Do not commit Telegram tokens or chat IDs

If a token is ever exposed, regenerate it using @BotFather

📡 Telegram Alerts Setup
To use Telegram alerts:

Create a bot using @BotFather

Send any message to the bot from your Telegram account

Open this URL in your browser to get your chat_id:

bash
Copy
Edit
https://api.telegram.org/bot<your_token>/getUpdates
Save TELEGRAM_TOKEN and CHAT_ID in the .env file

📁 Project Structure
File	Description
arbitrage_bot.py	Main script to detect arbitrage
telegram_alert.py	Handles Telegram alert sending
.env	Contains your private bot credentials
.gitignore	Prevents .env and cache files from uploading
requirements.txt	Python dependencies

📌 Notes
The bot currently monitors a single symbol (e.g., BTCUSDT)

You can extend it to check multiple pairs or integrate with other exchanges

📜 License
This project is licensed under the MIT License.
Feel free to fork, improve, and build upon it.

✉️ Contact
Maintained by @heshan909
Open an issue if you encounter bugs or want to suggest improvements.

yaml
Copy
Edit

---

### ✅ Final Step: Commit and Push

Once you’ve saved the new `README.md`, run:

```bash
git add README.md
git commit -m "Add complete README with setup and Telegram info"
git push origin main