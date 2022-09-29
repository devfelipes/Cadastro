import logging
from datetime import datetime

class Log():
    def __init__(self):
        self.date =datetime.today().strftime('%d-%m-%y')
        self.log = logging
        self.log.getLogger('oi')
        self.log.basicConfig(
            level=logging.DEBUG,
            encoding='UTF-8',
            format='%(asctime)s:(%(levelname)s):%(message)s',
            handlers=[logging.FileHandler(f'log\\log({self.date}).txt','a'),
            logging.StreamHandler()]
        )
    def error (self,print):
        self.log.error(print)
    def info(self,print):
        self.log.info(print)
    def warning (self,print):
        self.log.warning(print)
    def critical(self,print):
        self.log.critical(print)
    def debug (self,print):
        self.log.debug(print)