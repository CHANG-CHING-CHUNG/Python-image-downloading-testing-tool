import psycopg2
from db_class import db
from PIL import Image
import io
from os import walk
from ImageController import imageController
from MainController import mainController
import time
import logging





local_img_list = mainController.get_all_filenames("/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/測試用圖片/test-image")

# for img_name in img_list:
#   print(img_name)
#   returned_id = mainController.upload_img_to_database(img_name)
#   if not returned_id:
#     print("Upload failed")
#   print(f"Image: {img_name} upload succeeded")


# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)
# start_time = time.time()
# logging.info('測試開始')
# save_image_path = "/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/"
# limit = 1367

# logging.info(f'開始從資料庫拉取 {limit} 筆 byte 型式的圖片')
# remote_img_list = mainController.fetch_images_from_database_by_limit(limit)
# img_count = len(remote_img_list)
# logging.info(f'{img_count} 筆 byte 型式的圖片拉取結束')

# logging.info(f'開始將 {img_count} 筆 byte 型式的圖片轉成圖片格式並存進 {save_image_path} 資料夾')
# for img in remote_img_list:
#   img_name = img[0]
#   img_bytes = img[1]
#   img = mainController.read_image_from_bytes(img_name,img_bytes)
#   mainController.save_image_to_path(img,save_image_path,img.filename)
#   # if mainController.save_image_to_path(img,save_image_path,img.filename):
#   #     print(f"Image: {img_name} save succeeded")

# logging.info(f'{img_count} 筆圖片下載完畢')
# end_time = time.time()
# elapsed_time = start_time-end_time
# logging.info('測試結束')
# logging.info(f'花費時間: {elapsed_time}')

# print(local_img_list)

mainController.upload_img_url_to_database(local_img_list[-1])