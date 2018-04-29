import requests
from bs4 import BeautifulSoup
from glob import glob
from os.path import splitext
from PIL import Image
from io import BytesIO
import xlsxwriter
# 事先抓好圖片
import image_crawler
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('plan.xlsx')
worksheet = workbook.add_worksheet()
# 調整欄位寬度
worksheet.set_column(0,0,50)
worksheet.set_column(2,2,80)
# index of 全部資料
i = 0
# 該網站有10頁
for page in range(1,10):
	res = requests.get('https://www.chanchao.com.tw/laserexpo/visitorExhibitor.asp?page='+str(page))
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,"lxml")
	text_style = workbook.add_format({'text_wrap':1,'valign': 'top'})
	for para in soup.findAll('div',{"class":"right"}):
		worksheet.set_row(i,250)
		worksheet.write(i,2,para.text,text_style)
		i = i + 1
# 寫入EXCEL 檔案之中
for k in range(0,90):
	filename = 'images_new/logo'+str(k)+'.jpg'
	worksheet.insert_image(k,0, filename,{'positioning': 3})

workbook.close()








