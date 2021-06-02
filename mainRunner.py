import os   
import time
import subprocess
# 使用方式:
  # python ./databaseDownload.py [log 編號] [目標資料夾名稱]
  # 預設為 [log 編號 = "" ] [目標資料夾名稱 ="" ]
  # 預設資料夾: 
  # /home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/[目標資料夾名稱]
class Runner:
  def generate_commands(self,script_name, logs_num):
      start = "python "
      middle_str = "./{}.py {}"
      end = " &"
      command_arr=[]
      new__command_arr = []

      for k in range(1,logs_num +1 ):
        new_middle_str = middle_str.format(script_name, k)
        join_str = start + new_middle_str + " {}" + end
        command_arr.append(join_str)
      
      for j in range(0,len(command_arr)):
        new__command_arr.append(j)
      for m in range(0,len(command_arr)):
          new__command_arr[m] = command_arr[m].format(m+1)
      return new__command_arr

  def run_single_download(self,type,logs_num, times_to_run):
      for n in range(1,times_to_run + 1):
        if type == "db":
          os.system(f'python ./databaseDownload.py {logs_num} {n}')
        elif type == "url":
          os.system(f'python ./urlDownload.py {logs_num} {n}')

      if type == "db":
        os.system(f'python ./calTotalTime.py db {logs_num}')
      elif type == "url":
        os.system(f'python ./calTotalTime.py url {logs_num}')

      os.system(f'python ./deleteDownloadedImg.py')

  def run_multiple_download_same_time(self,type ,script_name, logs_num, times_to_run, sleep_seconds):
      new__command_arr = self.generate_commands(script_name, logs_num)

      for n in range(1,times_to_run + 1):
        command_str = " ".join(new__command_arr)
        
        if type == "db":
          print(command_str)
          os.system(command_str)
          time.sleep(sleep_seconds)
          os.system(f'python ./deleteDownloadedImg.py')
        elif type == "url":
          print(command_str)
          os.system(command_str)
          time.sleep(sleep_seconds)
          os.system(f'python ./deleteDownloadedImg.py')
        

      time.sleep(1)
      if type == "db":
        os.system(f'python ./calTotalTime.py db 1')
        os.system(f'python ./calTotalTime.py db 2')
        os.system(f'python ./calTotalTime.py db 3')
      elif type == "url":
        os.system(f'python ./calTotalTime.py url 1')
        os.system(f'python ./calTotalTime.py url 2')
        os.system(f'python ./calTotalTime.py url 3')
      
      os.system(f'python ./deleteDownloadedImg.py')


r = Runner()
r.run_multiple_download_same_time("db","databaseDownload", 3, 3,120)
# r.run_multiple_download_same_time("url","urlDownload", 3, 10, 30)


