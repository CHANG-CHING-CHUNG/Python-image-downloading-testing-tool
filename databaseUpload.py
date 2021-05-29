from MainController import mainController






local_img_list = mainController.get_all_filenames("/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/測試用圖片/test-image")

for img_name in local_img_list:
  print(img_name)
  returned_id = mainController.upload_img_to_database(img_name)
  if not returned_id:
    print("Upload failed")
  print(f"Image: {img_name} upload succeeded")