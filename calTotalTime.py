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

    def cal_average_cpu_ram(self,type,log_num):
      if type == "db":
        log = self.db_log
      elif type == "url":
        log = self.url_log
      f = open(log, "r")
      txt = f.read()
      download_result = re.findall("下載時 CPU 使用率: ([0-9][0-9,\.]+) %   記憶體使用率: ([0-9][0-9,\.]+) %",txt)
      save_result = re.findall("儲存時 CPU 使用率: ([0-9][0-9,\.]+) %   記憶體使用率: ([0-9][0-9,\.]+) %",txt)

      print(download_result)
      print(save_result)

      download_total_used_cpu = 0
      download_total_used_ram = 0
      save_total_used_cpu = 0
      save_total_used_ram = 0

      for n in range(len(download_result)):
        download_total_used_cpu += float(download_result[n][0])
        download_total_used_ram += float(download_result[n][1])

        save_total_used_cpu += float(save_result[n][0])
        save_total_used_ram += float(save_result[n][1])

      average_download_used_cpu = round((download_total_used_cpu / len(download_result)),2)
      average_download_used_ram = round((download_total_used_ram / len(download_result)),2)

      average_save_used_cpu = round((save_total_used_cpu / len(save_result)),2)
      average_save_used_ram = round((save_total_used_ram / len(save_result)),2)

      print(average_download_used_cpu)
      print(average_download_used_ram)

      logger = self.setup_logger(type,log)
      logger.info(f'下載時 cpu 平均使用率: {average_download_used_cpu} %  下載時 RAM 平均使用率: {average_download_used_ram} %')
      logger.info(f'儲存時 cpu 平均使用率: {average_save_used_cpu} %  儲存時 RAM 平均使用率: {average_save_used_ram} %')


current_date = datetime.datetime.now()
current_date = current_date.strftime("%Y-%m-%d")
# log_type = sys.argv[1]
# log_num = sys.argv[2]
# db_log = f"{current_date}-db-download-{log_num}.log"
# url_log = f"{current_date}-url-download-{log_num}.log"

db_log = f"2021-06-03-db-download-1.log"
url_log = f"2021-06-03-url-download-1.log"

calTime = CalTime(db_log, url_log)
# calTime.cal_average_time(log_type, log_num)
calTime.cal_average_cpu_ram("url",3)
