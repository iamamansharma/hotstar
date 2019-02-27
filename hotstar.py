from selenium import webdriver
import datetime
pth = input('path of webdriver')
d = webdriver.Chrome(pth)
d.get('https://www.hotstar.com/sports/cricket/australia-in-india-2019/india-vs-australia-m189946/live-streaming/2001710219')

n = datetime.datetime.now()
k = n +  datetime.timedelta(seconds = 540)
while True:		
	if datetime.datetime.now() == k:
		d.get('https://www.hotstar.com/sports/cricket/australia-in-india-2019/india-vs-australia-m189946/live-streaming/2001710219')
		n = datetime.datetime.now()
		k = n + datetime.timedelta(seconds = 540)

