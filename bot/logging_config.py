import logging
import json
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

class JSONFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "time": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage()
        })

logger = logging.getLogger("trading_bot")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("logs/trading.log")
    file_handler.setFormatter(JSONFormatter())
    logger.addHandler(file_handler)

logger.propagate = False