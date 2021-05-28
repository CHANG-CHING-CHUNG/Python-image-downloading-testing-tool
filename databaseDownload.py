import psycopg2
from db_class import db
from PIL import Image
import io
from os import walk
from ImageController import imageController
from MainController import mainController
import time
import logging
import datetime
current_date = datetime.datetime.now()
current_date = current_date.strftime("%Y-%m-%d")

logging.basicConfig(filename=current_date+'-db-download.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)
start_time = time.time()
logging.info('db 圖片下載測試開始')
save_image_path = "/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/"
limit = 1367

logging.info(f'開始從資料庫拉取 {limit} 筆 byte 型式的圖片')
remote_img_list = mainController.fetch_images_from_database_by_limit(limit)
img_count = len(remote_img_list)
logging.info(f'{img_count} 筆 byte 型式的圖片拉取結束')

logging.info(f'開始將 {img_count} 筆 byte 型式的圖片轉成圖片格式並存進 {save_image_path} 資料夾')
for img in remote_img_list:
  img_name = img[0]
  img_bytes = img[1]
  img = mainController.read_image_from_bytes(img_name,img_bytes)
  mainController.save_image_to_path(img,save_image_path,img.filename)
  # if mainController.save_image_to_path(img,save_image_path,img.filename):
  #     print(f"Image: {img_name} save succeeded")

logging.info(f'{img_count} 筆圖片下載完畢')
end_time = time.time()
elapsed_time = end_time - start_time
logging.info('測試結束')
logging.info(f'花費時間: {elapsed_time}')