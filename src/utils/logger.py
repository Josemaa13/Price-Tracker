# src/utils/logger.py
import logging
import os

def setup_logger():
    """Configures the logging system for the application."""
    # Ensure the logs directory exists
    logs_dir = os.path.join("data", "logs")
    os.makedirs(logs_dir, exist_ok=True)
    
    log_file = os.path.join(logs_dir, "scraper.log")
    
    # Configure the logging format
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'), # Saves to file
            logging.StreamHandler()                          # Also prints to terminal
        ]
    )
    return logging.getLogger(__name__)