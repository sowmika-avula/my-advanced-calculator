import logging
import os
from dotenv import load_dotenv

load_dotenv()


def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "calculator.log")

    # Clear any existing handlers
    logging.root.handlers = []

    # Set up logging configuration
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode="w"),  # Overwrite the file
            logging.StreamHandler(),
        ],
    )
