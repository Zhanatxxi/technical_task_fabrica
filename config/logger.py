import logging


def get_logger(name):
    """ return logger """
    logger = logging.getLogger(name)
    logger.setLevel('INFO')
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(c_handler)
    return logger
