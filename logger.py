from logging import getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO


LOG_DIR = "./executed.log"


def get_module_logger(module, verbose):
    logger = getLogger(module)
    logger = _set_handler(logger, StreamHandler(), False)
    logger = _set_handler(logger, FileHandler(LOG_DIR, encoding='utf-8'), verbose)
    logger.setLevel(DEBUG)
    logger.propagate = False
    return logger


def _set_handler(logger, handler, verbose):
    if verbose:
        handler.setLevel(DEBUG)
    else:
        handler.setLevel(INFO)
    handler.setFormatter(Formatter('%(asctime)s:[%(levelname)s]: %(message)s'))
    logger.addHandler(handler)
    return logger