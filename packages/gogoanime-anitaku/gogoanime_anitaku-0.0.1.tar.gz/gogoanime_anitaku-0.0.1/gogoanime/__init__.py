import os
import sys
import logging

__version__ = "0.1.0"

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = os.path.join(os.path.expanduser("~"),".logs")
log_filepath = os.path.join(log_dir,"gogoanime_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("gogoanime")
