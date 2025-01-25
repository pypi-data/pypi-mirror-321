from datetime import datetime
import time

def get_unix_timestamp() -> int:
    return int(time.time())

def get_formatted_timestamp() -> str:
    now = datetime.now()
    return now.strftime('%H:%M:%S %d:%m:%Y')
