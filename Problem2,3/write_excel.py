from glob import glob
from os.path import splitext
import os
from PIL import Image
from io import BytesIO
import xlsxwriter
# 外商已經抓好圖片
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('foregin.xlsx')
worksheet = workbook.add_worksheet()
# 調整欄位寬度
worksheet.set_column(0,0,50)
worksheet.set_column(2,2,80)
# index of 全部資料
# 讀進所有廠商資料
with open('keywords_sort.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
text_style = workbook.add_format({'text_wrap':1,'valign': 'top'})
for i in range(0,len(content)):
	filename = 'foreign_logo/logo'+str(i)+".png"
	worksheet.set_row(i,250)
	worksheet.insert_image(i,0, filename,{'positioning': 3})
	worksheet.write(i,2,content[i],text_style)
	i = i + 1
# # 寫入EXCEL 檔案之中 write into excel
# for k in range(0,54):
# 	filename = 'foregin_logo/logo'+str(k)+content[]
# 	worksheet.insert_image(k,0, filename,{'positioning': 3})

workbook.close()








