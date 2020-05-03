import os
import sys
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

app = Flask(__name__)

channel_access_token = os.environ('s7s9lN2bfAJNNPAQfoh0R2IMS2HYcoLcLJ3EIzCjf6bvi7DIkDMIpjL0zNJnPy+pFgTGdSZnJtbKZdC+2jVhLokj3rMcZUyl+aXviqejT1nmZNro4bYHCv6Nk6AwfqMMyNGjI7QEyYQToLLFh+1f+AdB04t89/1O/w1cDnyilFU=')
channel_secret = os.environ('523ef5d1e8822b5070a0457254b26609')

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

#Webhookからのリクエストのチェック
@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']

	body = request.get_data(as_test=True)
	app.logger.info("Request body: " + body)
 
    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='ワードウルフを始めますか？'))

if __name__ == "__main__":
	port = int(os.getenv("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
