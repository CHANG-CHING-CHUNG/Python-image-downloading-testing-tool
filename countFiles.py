from os import walk
from MainController import mainController
import os
from dotenv import load_dotenv
load_dotenv()

limit = os.getenv("LIMIT")
base_dir = os.getenv("SAVE_IMAGE_PATH")
dirs_list = []
for (dirpath, dirnames, filenames) in walk(base_dir):
    dirs_list.extend(dirnames)
    break

total_img_list = []

for directory_for_save_img in dirs_list:
    local_img_list = mainController.get_all_filenames(f"{base_dir}{directory_for_save_img}/")
    total_img_list.append(len(local_img_list))

is_img_missing = False
for count in total_img_list:
    if count != limit:
      is_img_missing = True
      break

if is_img_missing:
  print("有圖片遺失了!")
else:
  print("沒有圖片遺失")
