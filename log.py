import coloredlogs, logging

def setup_custom_logger():
    # create logger
    logger = logging.getLogger('project')
    logger.setLevel(logging.DEBUG)

    coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    coloredlogs.install(level='DEBUG')
    
    return logger