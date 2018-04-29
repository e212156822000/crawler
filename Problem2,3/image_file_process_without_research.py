import os
from PIL import Image
with open('keywords_sort.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
for i in range(0,len(content)):
	if "University" in content[i] or \
	 "Research" in content[i] or \
	 "NASA" in content[i] or \
	 "UCLA" in content[i] or \
	 "UCSD" in content[i]:
	 	pass
	else:
		for filename in os.listdir("./google_images/"+content[i]):
			print(filename)
			im = Image.open("./google_images/"+content[i]+"/"+filename)
			if(im.width > 330):
				width = 330
				ratio = float(width/im.width)
				height = int(im.height*ratio)
				new = im.resize((width,height), Image.BILINEAR)
				new.save('./research_images/logo'+str(i)+".png","PNG")
			else:
				im.save('./research_images/logo'+str(i)+".png","PNG")
		#im.save('./foreign_logo/logo'+str(i)+".png","PNG")
		# os.rename("./google_images/"+content[i]+"/"+filename, "./foregin_logo/logo"+str(i)+filename[-4:])