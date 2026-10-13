# making logger module

import logging
import os

def setup_logger(name: str)-> logging.Logger:
  """
  Create and returns a professional logger that outputs to both file console and inside 'log/' folder
  """

  # A. Creating logger object:
  logger = logging.getlogger(name)
  logger.setLevel(logging.INFO)

  # Preventing dublicate logs if setup_logger called multiple times

  if not logger.handlers:

    # B. Making logger folder automatically:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    os.makedirs(exist_ok=True)

    log_file_path = os.path.join(LOG_DIR, 'app.logs')

    # C. Making formatter:
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt = '%Y-%M-%D %H:%M:%S',
    )

    # D. Handler 1: Console handler
    console_handler = logging.Streamhandler()
    console_handler.setlevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # E. handler 2: file handler
    file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # F. Join Hanlders with loggers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

  return logger



