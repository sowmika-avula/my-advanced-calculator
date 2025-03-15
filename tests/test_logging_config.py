from calculator.logging_config import setup_logging
import logging
import os


def test_logging_config(tmp_path):
    # Test environment variables
    os.environ["LOG_LEVEL"] = "DEBUG"
    os.environ["LOG_FILE"] = str(tmp_path / "test.log")

    setup_logging()

    logger = logging.getLogger()
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 2  # File + Stream handlers
