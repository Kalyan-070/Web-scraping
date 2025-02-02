import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd

url='https://codegnan.com/'
page=r.get(url)
soup=bs(page.text)
data=soup.find('div',attrs={'class':'page-content'})
vb=data.text.split('\n')
sh=vb[vb.index('⭐ Our certification  programs ')+1:vb.index('Companies where  Our students got placed ')]
main_data=[i.strip() for i in sh if i!='']
sh_data=[i for i in main_data if i!='']
#print(sh_data[0:4])
locations=[]
durations=[]
courses=[]
description=[]
for i in range(0,len(sh_data),4):
	durations.append(sh_data[i].split('Duration: ')[-1])
	courses.append(sh_data[i+1])
	description.append(sh_data[i+2])
	locations.append(sh_data[i+3])
df=pd.DataFrame({'courses':courses,'Duration':durations,'Description':description,'Location':locations})
df.to_csv('codegnan_Scrape_data.csv')
print('Successfully Scrapped.....')


