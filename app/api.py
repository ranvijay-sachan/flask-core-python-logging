import logging
from app import app

logger = logging.getLogger()


@app.route('/')
def hello_world():
    logger.info('tessdlkdskdsckj')
    return 'Hello, World!'