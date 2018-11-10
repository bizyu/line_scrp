import urllib.request
from bs4 import BeautifulSoup
import json
import requests


# アクセス先URLとUAを設定
url = 'https://sports.yahoo.co.jp/news/list?id=jleague'
ua =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


# 記事取得関数
def getNews(word):

    # 下記はアクセス先に合わせて修正しスクレイピング
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find('div', attrs={'class': 'modBody'})
    topics = main.find_all(attrs={'class': 'linkMain'})

    # 該当記事カウント変数と結果格納リスト
    count = 0
    list = []

    # スクレイピング結果から引数wordを含む記事を結果リストに格納
    for topic in topics:
        if topic.contents[0].find(word) > -1:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1
    if count == 0:
        result.append("該当記事はありません")

    # リスト内の要素間に改行を挿入して返却
    result = '\n'.join(list)
    return result
