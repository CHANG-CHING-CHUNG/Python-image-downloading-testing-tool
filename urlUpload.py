from MainController import mainController
import os
from dotenv import load_dotenv
load_dotenv()

images_path = os.getenv("IMAGES_PATH")


local_img_list = mainController.get_all_filenames(images_path)
for img_name in local_img_list:
  print(img_name)
  returned_id = mainController.upload_img_url_to_database(img_name)
  if not returned_id:
    print("Upload failed")
  print(f"Image: {img_name} upload succeeded")