import urllib.request
from bs4 import BeautifulSoup
import json
import requests


# アクセス先URLとUAを設定
# url = 'https://sports.yahoo.co.jp/news/list?id=jleague'
url='http://gigazine.net/'
ua =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

# uaが必要なのはyahooだからで、gigazineはログイン必要ないからいらないかも
# この部分とどこから言葉を検索するかを書き換えればいいんとちゃう

# 記事取得関数
# def getNews(word):
# def/ getNews:

    # 下記はアクセス先に合わせて修正しスクレイピング
    # req = urllib.request.Request(url, headers={'User-Agent': ua})
    # html = urllib.request.urlopen(req)
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

    # topics = soup.find_all("div",{"class":"card"})
main = soup.find('div', attrs={'class': 'section'})
topics = main.find_all(attrs={'class':'span'})

    # main = soup.find('div', attrs={'class': 'modBody'})
    # topics = main.find_all(attrs={'class': 'linkMain'})

    # 該当記事カウント変数と結果格納リスト
count = 0
list = []

    # スクレイピング結果から引数wordを含む記事を結果リストに格納
for topic in topics:
        # name = topic.find("h2").a.string
        # print(name)
       # if topic.contents[0].find(word) > -1:
    list.append(topic.contents[0])
    list.append(topic.get('href'))
            # count += 1
    # if count == 0:
        # result.append("該当記事はありません")

    # リスト内の要素間に改行を挿入して返却
    result = '\n'.join(list)
    # return result

print(result)
