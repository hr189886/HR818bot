import time
from config.settings import LOG_FILE

QUEUE_FILE = "code_queue.txt"

def process_queue():
    try:
        with open(QUEUE_FILE, "r") as f:
            content = f.read().strip()
        if content:
            print("📥 Code received:", content)
            with open(LOG_FILE, "a") as log:
                log.write(content + "\n")
            with open(QUEUE_FILE, "w") as f:
                f.write("")
    except FileNotFoundError:
        pass

def start_listener():
    while True:
        process_queue()
        time.sleep(5)
