from PIL import Image
from db_class import db
import io
class ImageController:
    def read_image_from_bytes(self, img_name,img_bytes):
        img = Image.open(io.BytesIO(img_bytes))
        img.filename = img_name
        return img

    def read_image_from_img_url(self,img_name, img_url):
        img = Image.open(img_url+img_name)
        img.filename = img_name
        return img

    def convert_image_to_bytes(self, img):
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
    
    def save_image_to_path(self,img,path,img_name):
        try:
            img.save(path+img_name,format=img.format)
        except:
            return False
        return True
        
    def upload_image_to_database_in_bytes(self, img):
        img_bytes = self.convert_image_to_bytes(img)
        insert_query = "INSERT INTO image(image_name, image_data, mine_type) VALUES(%s,%s,%s) RETURNING id"
        query_var = (img.filename, img_bytes, img.format,)
        db.execute_query(insert_query, query_var)
        returned_id = db.fetchone()[0]
        return returned_id

imageController = ImageController()