import logging
import os
from datetime import datetime

# Create logs directory if not exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# current timestamp for log file
current_time = datetime.now().strftime('%y-%m-%d_%H-%M-%S')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(f"logs/test_log_{current_time}.log"), logging.StreamHandler()]
)