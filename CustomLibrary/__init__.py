# -*- coding: utf-8 -*-

from robot.api import logger

__version__ = 'Intial'

class CustomLibrary:
    """This is CustomLibrary.
    Add Library Documentation here for usage.
    """
    
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_DOC_FORMAT = "ROBOT"
    
    def __init__(self):
        pass
    
    def test_keyword(self, argument):
        """"""
        logger.info("Runing Keyword")
        logger.info("argument: {}".format(argument))
