import requests
from bs4 import BeautifulSoup
from glob import glob
from os.path import splitext
from PIL import Image
from io import BytesIO
# 把所有圖片urls爬下來，放到imageUrls裡面
imagesUrls = []
for page in range(1,10):
	res = requests.get('https://www.chanchao.com.tw/laserexpo/visitorExhibitor.asp?page='+str(page))
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,"lxml")
	for img in soup.findAll('img'):
		#new is used to be modified
		new = ""
		temp = img.get('src')
		print(temp[-10:])
		if temp[-10:] == "taiwan.png":#it will be duplicate
			pass
		elif temp[-11:] == "default.jpg":
			new = "https://www.chanchao.com.tw/laserexpo/"+ temp	
		elif temp[0:4] != "http":
			new = "https://www.chanchao.com.tw/laserexpo/" + temp[:-5] + 'B' + temp[-4:]
		else:
			new = temp[:-5] + 'B' + temp[-4:]
		if new != "":
			imagesUrls.append(new)
# debug
#print(imagesUrls)

k = 0
for jpg in imagesUrls:
	print(jpg)
	response = requests.get(jpg)
	im = Image.open(BytesIO(response.content))
	im.save('images_new/logo'+str(k)+".jpg","JPEG")
	k = k +1