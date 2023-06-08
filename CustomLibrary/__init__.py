# -*- coding: utf-8 -*-

from robot.api import logger

__version__ = 'Intial'


class CustomLibrary:
    """This is CustomLibrary. Add Library Documentation here for usage."""
    
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_DOC_FORMAT = "ROBOT"
    
    def __init__(self):
        """Constructor not initialized"""
        pass
    
    def test_keyword(self, argument=None):
        """Test Keyword Accepting optional arguments"""
        logger.info("Runing Keyword")
        logger.info("argument: {}".format(argument))
    
    def test_keyword2(self):
        """Dummy keyword with no arguments"""
        ## Add your code logic here
        pass
    
    def _private_keyword(self):
        """Private method which will not be displayed/Called in IDE"""
        ## Add your code logic here
        pass