from flask import Flask
from flask_restful import Resource, Api
import psycopg2
from db_class import db
from PIL import Image
import io
from ImageControler import imageControler

app = Flask(__name__)
api = Api(app)

# img = Image.open("test1.jpg")
# print(img.filename)
# img_byte_arr = io.BytesIO()
# img.save(img_byte_arr, format=img.format)
# img_byte_arr = img_byte_arr.getvalue()
# print(img_byte_arr)

# file = open("test1.jpg",'rb')
# filedata = file.read()

# insert_query = ("INSERT INTO image(image_name, image_data, mine_type) VALUES(%s,%s)", (img.filename, img_byte_arr, img.format))
# db.execute_query("INSERT INTO image(image_name, image_data, mine_type) VALUES(%s,%s,%s)", (img.filename, img_byte_arr, img.format))

query_image_data = "select image_name, image_data,mine_type from image where image_name = %s"
image_name = "test1.jpg"
db.execute_query(query_image_data, (image_name,))
f = db.fetchone()
test_img = imageControler.read_image_from_bytes(f[1],"1q2w.jpg")
imageControler.save_image_to_path(test_img,"/home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/","111.jpg")

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=False)