✅ HR818bot — Full Project Starter Structure (Updated with Multi‑Exchange Support)

─── FOLDER STRUCTURE ─────────────────────────────

HR818bot/

├── main.py

├── requirements.txt

├── code_queue.txt

├── config/

│   └── settings.py  ← UPDATED (multi‑exchange, fallback)

├── core/

│   ├── listener.py

│   └── file_writer.py

├── telegram/

│   ├── bot.py

│   └── commands.py

├── trading/

│   ├── strategy.py

│   ├── validator.py

│   └── risk.py

├── logs/

│   └── history.log

└── utils/

└── helpers.py

─── FILE CONTENTS ────────────────────────────────

config/settings.py

BOT_TOKEN = "8038780034:AAHnevnCOlk0ZoHHj4Lqv3_aiLhQoSty3t0" ADMIN_USER_ID = 7109221382

✅ Supported Trading Pairs (extend anytime)

ASSETS = [ "BTC/USDT",  # Bitcoin "ETH/USDT",  # Ethereum "XAUT/USDT"  # Tether Gold ]

✅ Exchange Fallback Logic

FIRST element is primary – if its API fails the bot auto‑switches to the next.

EXCHANGES = [ "mexc",      # your main perpetual account "binance",   # automatic fallback ]

RISK_LIMIT = 2               # Max 2% capital per trade CONFIDENCE_THRESHOLD = 85    # Trade only if ≥85% confirmed LOG_FILE = "logs/history.log"

main.py

from core.listener import start_listener

if name == "main": print("🔄 HamidBot Starting …") start_listener()

core/listener.py  (minimal placeholder – logic will grow)

import time from config.settings import LOG_FILE

QUEUE_FILE = "code_queue.txt"

def process_queue(): try: with open(QUEUE_FILE, "r") as f: content = f.read().strip() if content: print("📥 Code received:", content) with open(LOG_FILE, "a") as log: log.write(content + "\n") with open(QUEUE_FILE, "w") as f: f.write("") except FileNotFoundError: pass  # queue not created yet

def start_listener(): while True: process_queue() time.sleep(5)

requirements.txt (partial – will expand)

python-telegram-bot==13.15 requests

