import requests
from bs4 import BeautifulSoup
#simple version
res = requests.get('https://www.chanchao.com.tw/laserexpo/visitorExhibitor.asp?page=1')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,"lxml")
for para in soup.findAll('div',{"class":"right"}):
	print(para.text)
	# print(para.find('h3').text)
	# print(para.find('a').get('href'))