import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
log_file = os.path.join(LOG_DIR, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Configure logger
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

def get_logger():
    return logger
