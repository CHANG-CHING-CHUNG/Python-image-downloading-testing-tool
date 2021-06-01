import re
import functools
import logging
import sys
import datetime

class CalTime:
    def __init__(self, db_log, url_log):
      self.db_log = db_log
      self.url_log = url_log
      self.formatter = '%(asctime)s - %(levelname)s - %(message)s'
      self.datefmt='%Y-%m-%d %H:%M:%S'
    def setup_logger(self,name, log_file, level=logging.INFO):
      """To setup as many loggers as you want"""

      handler = logging.FileHandler(log_file)    
      formatter = logging.Formatter(self.formatter,self.datefmt)    
      handler.setFormatter(formatter)

      logger = logging.getLogger(name)
      logger.setLevel(level)
      logger.addHandler(handler)

      return logger

    def cal_average_time(self,type,log_num):
      if type == "db":
        log = self.db_log
      elif type == "url":
        log = self.url_log
      f = open(log, "r")
      txt = f.read()
      result = re.findall("花費時間: [0-9][0-9,\.]+",txt)

      for n in range(len(result)):
        spent_time = re.findall("[0-9][0-9,\.]+",result[n])[0]
        result[n] = float(spent_time)

      total_spent_time = functools.reduce(lambda a, b: a+b, result)
      average_time = round((total_spent_time / len(result)),2)

      logger = self.setup_logger(type,log)
      logger.info(f'合計平均時間: {average_time}')
    


current_date = datetime.datetime.now()
current_date = current_date.strftime("%Y-%m-%d")
log_type = sys.argv[1]
log_num = sys.argv[2]
db_log = f"{current_date}-db-download-{log_num}.log"
url_log = f"{current_date}-url-download-{log_num}.log"
calTime = CalTime(db_log, url_log)
calTime.cal_average_time(log_type, log_num)
