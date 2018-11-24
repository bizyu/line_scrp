from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage,
    FlexSendMessage, BubbleContainer, CarouselContainer, TextSendMessage
)

import urllib.request
import os
import json
import sccate as sc


import re
import sys
from argparse import ArgumentParser
from re import Match
from jinja2 import Environment, FileSystemLoader, select_autoescape
import qiita


app = Flask(__name__)


#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


template_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)


class TextPatternHandler:

    def __init__(self):
        self.handlers = []

    def add(self, pattern: str):
        def decorator(func):
            self.handlers.append((re.compile(pattern), func))
            return func
        return decorator

    def handle(self, event: MessageEvent):

        text = event.message.text

        for pattern, func in self.handlers:
            m = pattern.match(text)
            if m:
                func(event, m)
                return True

        return False


text_pattern_handler = TextPatternHandler()

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    except LineBotApiError as e:
        app.logger.exception(f'LineBotApiError: {e.status_code} {e.message}', e)
        raise e

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

    try:
        # ユーザー入力event
        replied = text_pattern_handler.handle(event)

        if not replied:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage('ちょっと何言ってるかわからない')
            )

    except Exception:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage('エラーです')
        )
        raise

@text_pattern_handler.add(pattern=r'^items$')
def reply_items(event: MessageEvent, match: Match):

    items = qiita.get_items(10)
    # 表示のテンプレトをディレクトリから取得
    template = template_env.get_template('items.json')
    data = template.render(dict(items=items))

    print(data)

    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(
            alt_text="items",
            # dataを入力してカルーセルで応答
            contents=CarouselContainer.new_from_json_dict(json.loads(data))
        )
    )

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
