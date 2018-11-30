import urllib.request
from bs4 import BeautifulSoup
import json
import requests
import tes

result = tes.rank("人気記事")

code = {
"type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "GIGAZINE ranking",
        "weight": "bold",
        "color": "#000000",
        "size": "xl"
      }
    ]
  },
   "hero": {
    "type": "image",
    "url": result[0][2],
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": result[0][1]
    }
  },

  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": result[0][0],
                # "wrap": true,
                "color": "#666666",
                "weight": "bold",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": "https://gigazine.net/"
                }
            },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
},
    {
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "GIGAZINE ranking",
        "weight": "bold",
        "color": "#000000",
        "size": "xl"
      }
    ]
  },
   "hero": {
    "type": "image",
    "url": result[1][2],
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": result[1][1]
    }
  },

  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": result[1][0],
                # "wrap": true,
                "color": "#666666",
                "weight": "bold",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": "https://gigazine.net/"
                }
            },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
},
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "GIGAZINE ranking",
        "weight": "bold",
        "color": "#000000",
        "size": "xl"
      }
    ]
  },
   "hero": {
    "type": "image",
    "url": result[2][2],
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": result[2][1]
    }
  },

  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": result[2][0],
                # "wrap": true,
                "color": "#666666",
                "weight": "bold",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": "https://gigazine.net/"
                }
            },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
},
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "GIGAZINE ranking",
        "weight": "bold",
        "color": "#000000",
        "size": "xl"
      }
    ]
  },
   "hero": {
    "type": "image",
    "url": "https://i.gzn.jp/img/2018/11/28/how-melt-gold-room-temperature/00_m.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },

  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "常温で溶けるはずのない「金」を室温でも簡単に溶かす方法が発見される",
                # "wrap": true,
                "color": "#666666",
                "weight": "bold",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": "https://gigazine.net/"
                }
            },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
},
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "GIGAZINE ranking",
        "weight": "bold",
        "color": "#000000",
        "size": "xl"
      }
    ]
  },
   "hero": {
    "type": "image",
    "url": "https://i.gzn.jp/img/2018/11/28/how-melt-gold-room-temperature/00_m.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },

  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "常温で溶けるはずのない「金」を室温でも簡単に溶かす方法が発見される",
                # "wrap": true,
                "color": "#666666",
                "weight": "bold",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": "https://gigazine.net/"
                }
            },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
  ]
}


f = open("templates/temp.json",'w')
# json.dict=json.load(f)
json.dump(code,f,indent=4)
# f.write(str(code))


