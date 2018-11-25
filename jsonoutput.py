import urllib.request
from bs4 import BeautifulSoup
import requests
import json

url = "http://gigazine.net/"

# response = requests.get(url).text
# soup = BeautifulSoup(response, 'html.parser')
# tagtag = soup.find_all("div",{"class":"card"})



code ={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            # // "text"にgigazine記事タイトルを表示
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "wrap": "true"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Go",
              # // 以下urlに記事リンクを張る
              "uri": url
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Hello, World!",
            "wrap": "true"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Go",
              "uri": "https://gigazine.net/news/20181124-cyber-terrorism-scenario/"
            }
          }
        ]
      }
    }
  ]
}


f = open('templates/j1.json', 'w')
# json_dict=json.load(f)
json.dump(code,f,indent=4)