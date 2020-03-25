import requests
from bs4 import BeautifulSoup as soup

url='https://www.mohfw.gov.in/'
req=requests.get(url)
soup=soup(req.text,'lxml')
index=[]
state_name=[]
confirmed_cases_indian=[]
confirmed_cases_foreign=[]
cured=[]
deaths=[]



table_class=soup.find_all(class_='table table-striped table-dark')[7]
i=0
for element in table_class.find_all('tr'):
	if i < 26:
		table_row=element.find_all('td')
		x=0
		for td in table_row:
			if x==0:
				index.append(int(td.string))
				x=x+1
			elif x==1:
				state_name.append(td.string)
				x=x+1
			elif x==2:
				confirmed_cases_indian.append(int(td.string))
				x=x+1
			elif x==3:
				confirmed_cases_foreign.append(int(td.string))
				x=x+1
			elif x==4:
				cured.append(int(td.string))
				x=x+1
			elif x==5:
				deaths.append(int(td.string))
				x=x+1
		i=i+1		

for i in range(len(index)):
	print(index[i])
	print(state_name[i])
	print(confirmed_cases_indian[i])
	print(confirmed_cases_foreign[i])
	print(cured[i])
	print(deaths[i])
	print('\n\n')