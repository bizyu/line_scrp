from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage,
    FlexSendMessage, BubbleContainer, CarouselContainer
)

import urllib.request
import os
import json
import sccate as sc


from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)


#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


# -----------------
template_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)
# -----------------

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

categ = "please choice categ\n" \
            "モバイル\n"\
            "ソフトウェア\n"\
            "ネットサービス\n"\
            "ウェブアプリ\n"\
            "ハードウェア\n"\
            "乗り物\n"\
            "サイエンス\n"\
            "生き物\n"\
            "動画\n"\
            "映画\n"\
            "マンガ\n"\
            "アニメ\n"\
            "ゲーム\n"\
            "デザイン\n"\
            "アート\n"\
            "食\n"\
            "メモ"
            


# メッセージリプライ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # ユーザからの検索ワードを取得
    word = event.message.text

    # 記事取得関数を呼び出し
    result = sc.getNews(word)



#この後おすすめでpv数から記事取得
# 応答メッセージ（記事検索結果）を送信
    if word == "hello":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(categ))
        )  
    elif word=="items":
        template = template_env.get_template('test.json')
        data = template.render(dict(items=test))
        # name_list = ["honoka","eri","kotori","umi","rin","maki","nozomi","hanayo","niko"]
        # for name in name_list:
        #     print("{0:6s} 身長：{1}cm BWH: ".format(name,json_data[name]["height"]),end="\t")
        #     for i in range(len(json_data[name]["BWH"])):
        #         print("{}".format(json_data[name]["BWH"][i]),end="\t")
        #     print()



        line_bot_api.reply_message(
        event.reply_token,
        # ===================================================
        FlexSendMessage(
            alt_text="items",
            # dataを入力してカルーセルで応答
            contents=BubbleContainer.new_from_json_dict(json.loads(data))
        )
# ----------------------------------------------------------------
            
        )

    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result)
        )


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
