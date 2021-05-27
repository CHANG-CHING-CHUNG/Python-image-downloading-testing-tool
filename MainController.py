import psycopg2
from db_class import db
from PIL import Image
import io
from os import walk
from ImageController import imageController


class MainController:

  def __init__(self, images_path, save_image_path):
    self.images_path = images_path
    self.save_image_path = save_image_path

  def get_all_filenames(self, directory_path):
      filenames_list = []
      for (dirpath, dirnames, filenames) in walk(directory_path):
        filenames_list.extend(filenames)
        break
      return filenames_list

  def upload_img_to_database(self, img_name):
      img = Image.open(self.images_path + "/" + img_name)
      img.filename = img.filename.split("/")[-1]
      returned_id = imageController.upload_image_to_database_in_bytes(img)
      return returned_id

  def fetch_one_image_from_database(self,image_name):
      query_image_data = "select image_name, image_data,mine_type from image where image_name = %s"
      db.execute_query(query_image_data, (image_name,))

      image_bytes = db.fetchone()

      image_name = image_bytes[0]
      image_bytes = image_bytes[1]

      image = imageController.read_image_from_bytes(image_name,image_bytes)
      return image

  def fetch_images_from_database_by_limit(self,limit):
      query_image_data = "select image_name, image_data,mine_type from image limit %s"
      db.execute_query(query_image_data, (limit,))

      image_bytes_arr = db.fetchall()

      return image_bytes_arr

  def save_image_to_path(self,img,path,img_name):
      result = imageController.save_image_to_path(img, path, img_name)
      return result

  def read_image_from_bytes(self, img_name,img_bytes):
      img = imageController.read_image_from_bytes(img_name,img_bytes)
      return img

images_path = "/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/測試用圖片/test-image"
save_image_path = "/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/"

mainController = MainController(images_path,save_image_path)