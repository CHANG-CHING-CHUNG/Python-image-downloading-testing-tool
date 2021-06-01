import shutil
import os
from dotenv import load_dotenv
load_dotenv()

save_image_path = os.getenv("SAVE_IMAGE_PATH")
dir_array = []

for n in range(1,11):
  dir_array.append(save_image_path + str(n))


for dir in dir_array:
  print(dir)
try:
  for dir in dir_array:
    shutil.rmtree(dir)
    os.makedirs(dir)
  print("所有圖片移除成功")
except:
  for dir in dir_array:
    os.makedirs(dir)