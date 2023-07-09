import os
import logging
import sys

logging_srt = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=logging_srt, 
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger()