import logging


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('[ %(asctime)s ] [ %(levelname)-5s ] %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)

client_logger = setup_logger('clientLogger', r'..\RembursementProject1\AccessLogs.log')
post_logger = logging.getLogger('clientLogger')