import urllib.request
from bs4 import BeautifulSoup
import requests
import json

url = "http://gigazine.net/"

def getNews(word):
	global result
	response = requests.get(url).text
	soup = BeautifulSoup(response, 'html.parser') # BeautifulSoupの初期化
	tagtag = soup.find_all("div",{"class":"card"})

    # 該当記事カウント変数と結果格納リスト
	count = 0
	list = []
	result=[]
	contents=[]

	for tag in tagtag:
		categgg=tag.find("div",{"class":"date"}).find("span",{"class":"catab"})
		# if tag.contents[0].find(word) > -1:
		# if tag.span.contents[0].find(word) > -1:
		# 	list.append(tag.span.contents[0])
		if categgg.contents[0].find(word) > -1:
			list.append(tag.contents[0])
			list.append(tag.a.get('href'))
			count += 1
		if count == 0:
			result.append("該当記事はありません") 

	list=[str(i) for i in list]
	result = '\n'.join(list)
	return result

# word="動画"
# result = getNews(word)
# print(result)