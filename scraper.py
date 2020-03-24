from bs4 import BeautifulSoup as soup
import requests
import os
import urllib

req = requests.get("https://www.hindustantimes.com/topic/coronavirus")
soup=soup(req.text, 'lxml')

title=[]
link=[]
description=[]
imgUrl=[]


for element in soup.find_all(class_="authorListing"):
	for Desc in element.find_all(class_='para-txt'):
		link.append(Desc.a['href'])
		description.append(Desc.text)

	for Title in element.find_all(class_='media-heading headingfour'):
		title.append(Title.a['title'])

	for list_images in element.find_all(class_='media-img'):
		imgUrl.append(list_images.a.img["data-src"])
		
"""
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://icecat.biz/p/toshiba/pscbxe-01t00een/satellite-pro-notebooks-4051528049077-Satellite+Pro+C8501GR-17732197.html"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("div", {"class":"thumb-pic"})
for img in imgs:
        imgUrl = img.a['href'].split("imgurl=")[1]
        urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))
"""
'''
print(len(title))
print(len(description))
print(len(link))
print(len(imgUrl))
'''
