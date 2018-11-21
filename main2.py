from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import urllib.request
import os
import json
import sccate as sc


app = Flask(__name__)


#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


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


# メッセージリプライ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # ユーザからの検索ワードを取得
    word = event.message.text

    # 記事取得関数を呼び出し
    result = sc.getNews(word)

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

#この後おすすめでpv数から記事取得
# 応答メッセージ（記事検索結果）を送信
    if word == "hello":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(categ))
        )  
    elif word == "サイエンス":
        event.reply_token,
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.gzn.jp/img/2018/11/21/modified-virus-kill-cancer-cells/00.jpg',
                        title='this is menu1',
                        text='description1',
                        actions=[
                            PostbackAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageAction(
                                label='message1',
                                text='message text1'
                            ),
                            URIAction(
                                label='uri1',
                                uri='https://gigazine.net/news/20181121-modified-virus-kill-cancer-cells/'
                            )
                        ]
                    ),
                    # CarouselColumn(
                    #     thumbnail_image_url='https://example.com/item2.jpg',
                    #     title='this is menu2',
                    #     text='description2',
                    #     actions=[
                    #         PostbackAction(
                    #             label='postback2',
                    #             text='postback text2',
                    #             data='action=buy&itemid=2'
                    #         ),
                    #         MessageAction(
                    #             label='message2',
                    #             text='message text2'
                    #         ),
                    #         URIAction(
                    #             label='uri2',
                    #             uri='http://example.com/2'
                    #         )
                    #     ]
                    # )
                ]
            )
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
