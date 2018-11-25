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
                  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                  "wrap": """true"""
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
                    "uri": "https://qiita.com/unbabel/items/1cf05f2a2be3d6fb3388"
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
                  "wrap": """true"""
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
                    "uri": "https://qiita.com/unbabel/items/1cf05f2a2be3d6fb3388"
                  }
                }
              ]
            }
          }
        ]
      }


f = open('templates/j1.json', 'w')
# # json_dict=json.load(f)
json.dump(code,f,indent=4)

# f.write(str(code))