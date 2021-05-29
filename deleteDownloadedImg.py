import shutil
import os

base_dir = "/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/"
dir_array = []

for n in range(1,11):
  dir_array.append(base_dir + str(n))


for dir in dir_array:
  print(dir)
try:
  for dir in dir_array:
    shutil.rmtree(dir)
    os.makedirs(dir)
except:
  for dir in dir_array:
    os.makedirs(dir)


