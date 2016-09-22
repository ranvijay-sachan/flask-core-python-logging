from app import app

from logging.config import dictConfig
from logly.logging_config import logging_config

dictConfig(logging_config)

app.run()