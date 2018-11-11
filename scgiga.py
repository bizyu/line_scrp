import urllib.request
from bs4 import BeautifulSoup
import requests
import json

url = "http://gigazine.net/"


def getNews(word):
	global result
	# TODO1 requestsで、指定されたURLのHTMLを取得してください。
	response = requests.get(url).text
	# print(response)

	soup = BeautifulSoup(response, 'html.parser') # BeautifulSoupの初期化
	# print(soup.prettify())

	tags = soup.find_all("h2")
	# print(tags)

	categ = soup.find_all("span",{"class":"catab"})
	# print(categ)

	tagtag = soup.find_all("div",{"class":"card"})
	# print(tagtag)

	# # データフレームを作成してください。列名は、name, urlです。
	columns = ["name", "url","categ"]
	# df2 = pd.DataFrame(columns=columns)

    # 該当記事カウント変数と結果格納リスト
	count = 0
	list = []
	result=[]
	contents=[]

	#gigazineのジャンル分けと公開日時を記録して追加したい。どちらか一つできればまずは好い
	#category は取得できたけど更新されないな。
	# # # 記事名と記事URLをデータフレームに追加してください

	for tag in tagtag:
		# print(word)	
		# wordは渡せている
		#findできない
		# print(tag)
		# if tag.contents[0].find(word) > -1:
		if tag.span.contents[0].find(word) > -1:
			# print(tag)
			# list.append(tag.find("h2").a.get("href"))
			# list.append(tag.find("span"))
			list.append(tag.span.contents[0])
			list.append(tag.get('href'))
	  		# name = tag.find("h2").a.string
	  		# url = tag.find("h2").a.get("href")
	  		# cat = tag.find("div",{"class":"date"}).find("span",{"class":"catab"}).string
			count += 1
			print(list)
	  # se = pd.Series([name, url,cat], columns)
		if count == 0:
			result.append("該当記事はありません")
			# result.append("街灯記事無")
	  # print(name,cat)
	  # df2 = df2.append(se, columns)
	     # リスト内の要素間に改行を挿入して返却
		# print(list)  

	list=[str(i) for i in list]
	result = '\n'.join(list)
	return result


# word = "アメリカ"
# print(1)
# result=getNews(word)
# print(2)
# print(str(result))