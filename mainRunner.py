import os   

# 使用方式:
# python ./databaseDownload.py [log 編號] [目標資料夾名稱] [要從資料庫撈的 LIMIT]
# 預設為 [log 編號 = "" ] [目標資料夾名稱 ="" ] [要從資料庫撈的 LIMIT = 1]
# 預設資料夾: 
# /home/john/桌面/工作/測試/減少檔案搬移避免檔案遺失測試/下載圖片區/[目標資料夾名稱]
for n in range(1,11):
  # os.system(f'python ./databaseDownload.py 1 {n} 1000')
  os.system(f'python ./urlDownload.py 1 {n} 1000')

# os.system('python ./databaseDownload.py 1 1 & python ./urlDownload.py 1 2')


