import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

logger = logging.getLogger("calculator")
logger.setLevel(logging.INFO)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch_fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
ch.setFormatter(ch_fmt)

# Rotating file handler (1MB x 3)
fh = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
fh.setLevel(logging.INFO)
fh_fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
fh.setFormatter(fh_fmt)

if not logger.handlers:
    logger.addHandler(ch)
    logger.addHandler(fh)