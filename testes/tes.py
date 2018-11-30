import urllib.request
from bs4 import BeautifulSoup
import json
import requests

url = "http://gigazine.net/"

def rank(word):
	if word=="人気記事":
		html = urllib.request.urlopen(url)
		soup = BeautifulSoup(html, "html.parser")

				# gigazineサイトの常に最新記事のurlを取り出す
		geturl = soup.find('div', attrs={'id': 'section'}).h2.a.get("href")
				# gettitle = soup.find('div', attrs={'id': 'section'}).h2.a.get("title")

				# 最新記事を開き、人気記事一覧を取得
		url2= geturl
		html2 = urllib.request.urlopen(url2)
		soup2 = BeautifulSoup(html2, "lxml")

		result=[]
		rank = soup2.find('div',id='ranking-entry')
		rankli=rank.find_all('a')

		for ui in rankli:
			getu=ui.get("href")
			gett = ui.text
			
			# print(getu)
			url3= url[:-1]+getu
			html3 = urllib.request.urlopen(url3)
			soup3 = BeautifulSoup(html3, "lxml")
			getcnt = soup3.find('div',{'class':'cntimage'})
			getimg = getcnt.find('img').get('src')
			print(getimg)
			result.append([gett,getu,getimg])

	# for i in range(ranklist):
	# 	for i in range(0,int(len(result))):
	# 		print(result[i][0],result[i][1],"\n")
	
	return result

# result=rank("人気記事")
# for i in range(0,int(len(result))):
# 	print(result[i][2],"\n")