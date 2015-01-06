# log_tools.py
#
# Author: Daniel Clark, 2014

'''
This module contains functions which help set up logging for python
coding and scripts.
'''

# Setup log file
def setup_logger(logger_name, log_file, level, to_screen=False):
    '''
    Function to initialize and configure a logger that can write to file
    and (optionally) the screen.

    Parameters
    ----------
    logger_name : string
        name of the logger
    log_file : string
        file path to the log file on disk
    level : integer
        indicates the level at which the logger should log; this is
        controlled by integers that come with the python logging
        package. (e.g. logging.INFO=20, logging.DEBUG=10)
    to_screen : boolean (optional)
        flag to indicate whether to enable logging to the screen

    Returns
    -------
    logger : logging.Logger object
        Python logging.Logger object which is capable of logging run-
        time information about the program to file and/or screen
    '''

    # Import packages
    import logging

    # Init logger, formatter, filehandler, streamhandler
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s : %(message)s')

    # Write logs to file
    fileHandler = logging.FileHandler(log_file)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    # Write to screen, if desired
    if to_screen:
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

    # Return the logger
    return logger
