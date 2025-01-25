__author__ = "Alex Ackerman"
__copyright__ = "Copyright 2025, Alex Ackerman"
__credits__ = ["Alex Ackerman"]
__license__ = "GPL"
__version__ = "0.2"
__date__ = "January 18, 2025"
__maintainer__ = "Alex Ackerman"
__status__ = "Production"

from datetime import datetime
from typing import Union

class Logger():
    def __init__(self, level : Union[int, str] = "INFO", header : str = None):
        """
        Initialize the Logger class.

        Args:
            level (Union[int, str], optional): The log level. Defaults to "INFO".
            header (str, optional): The message header. Defaults to None.
        """
        self.white      = "\033[0;37m"
        self.blue       = "\033[0;34m"
        self.cyan       = "\033[0;36m"
        self.green      = "\033[0;32m"
        self.yellow     = "\033[0;33m"
        self.red        = "\033[0;31m"
        self.magenta    = "\033[0;35m"
        self.reset      = "\033[0m"
        self.orange = "\033[38;5;208m"
        self.DEBUG = 0
        self.INFO = 1
        self.ATTENTION = 2
        self.WARNING = 3
        self.ERROR = 4
        self.CRITICAL = 5

        if header == None:
            self.header = ""
        else:
            self.header = header

        if type(level) == str:
            if level.upper() == "DEBUG":
                level = 0
            elif level.upper() == "INFO":
                level = 1
            elif level.upper() == "ATTENTION":
                level = 2
            elif level.upper() == "WARNING":
                level = 3
            elif level.upper() == "ERROR":
                level = 4
            elif level.upper() == "CRITICAL":
                level = 5
            else:
                self.__logger_msg("Invalid log level - defaulting to 'INFO'")
                level = 1
        elif type(level) == int:
            if level < 0 or level > 5:
                self.__logger_msg("Invalid log level - defaulting to 'INFO'")
                level = 1
            else:
                self.__logger_msg("Log level set to: " + str(level))
                self.level = level

        self.enabled = True

    def __logger_msg(self, message):
        
        string  = self.orange         + "LOGGER MESSAGE: " + message + self.reset
        print(string)

    def set_message_header(self, header):
        """
        Set the message header.
        Args:
            header (str): The message header.
        """
        self.__logger_msg("Message header set to: " + header)
        self.header = header

    def enable_logging(self):
        """
        Enable logging.
        """
        self.enabled = True
        self.__logger_msg("Logging enabled")

    def disable_logging(self):
        """
        Disable logging.
        """
        self.__logger_msg("Logging disabled")
        self.enabled = False
        
    def debug(self, message):
        """
        Log a debug message.
        Args:
            message (str): The message to log.
        """
        if self.level == 0 and self.enabled:
            string  = f"{self.white}{self.__datecode()}    DEBUG: {self.header}: {message}{self.reset}"
            print(string)
    
    def info(self, message):
        """
        Log an info message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 1 and self.enabled:
            string  = f"{self.cyan}{self.__datecode()}     INFO: {self.header}: {message}{self.reset}"
            print(string)
        
    def attention(self, message):
        """
        Log an attention message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 2 and self.enabled:
            string  = f"{self.green}{self.__datecode()}ATTENTION: {self.header}: {message}{self.reset}"
            print(string)
        
    def warning(self, message):
        """
        Log a warning message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 3 and self.enabled:
            string  = f"{self.yellow}{self.__datecode()}  WARNING: {self.header}: {message}{self.reset}"
            print(string)
        
    def error(self, message):
        """
        Log an error message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 4 and self.enabled:
            string  = f"{self.red}{self.__datecode()}    ERROR: {self.header}: {message}{self.reset}"
            print(string)
        
    def critical(self, message):
        """
        Log a critical message.
        Args:
            message (str): The message to log.
        """
        if self.level <= 5 and self.enabled:
            string  = f"{self.magenta}{self.__datecode()} CRITICAL: {self.header}: {message}{self.reset}"
            print(string)
        
    def __datecode(self):
        """
        Get the date code.
        Returns:
            str: The date code.
        """
        now = datetime.now()
        date = now.strftime("%m/%d/%Y %H:%M:%S.%f ")
        return(date)
    
    def set_level(self, level):
        """
        Set the log level.
        Args:
            level (int): The log level.
        """
        self.level = level
        
if __name__ == "__main__":
    logger = Logger()
    logger.set_level(logger.DEBUG)
    logger.set_message_header("Test Logger")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.attention("This is an attention message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.disable_logging()
    logger.debug("This message won't be printed")
    logger.info("This message won't be printed")
    logger.attention("This message won't be printed")
    logger.warning("This message won't be printed")
    logger.error("This message won't be printed")
    logger.critical("This message won't be printed")
    logger.enable_logging()

                