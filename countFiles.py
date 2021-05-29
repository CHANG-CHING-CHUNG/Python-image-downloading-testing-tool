from os import walk
from MainController import mainController

limit = 1000
base_dir = "/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區"

dirs_list = []
for (dirpath, dirnames, filenames) in walk(base_dir):
    dirs_list.extend(dirnames)
    break

total_img_list = []

for directory_for_save_img in dirs_list:
    local_img_list = mainController.get_all_filenames(f"/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/{directory_for_save_img}/")
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
