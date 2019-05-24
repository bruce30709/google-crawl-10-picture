import requests
from bs4 import BeautifulSoup
import os
from urllib import urlretrieve
import sys

url='https://www.google.com/search?q=twice%20momo&source=lnms&tbm=isch'
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
photo_list=soup.select('img')
#print(soup.prettify())
x=1
for photo in photo_list:
	#print(photo["src"])
	local = os.path.join("/home/bruce/Desktop/momo/%s.jpg" %x)
	urlretrieve(photo["src"],local)
	x+=1
	
