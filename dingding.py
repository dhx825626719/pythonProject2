# Python实用宝典
# 2021/11/13
import json
import hashlib
import base64
import hmac
import os
import time
import requests
from urllib.parse import quote_plus


class Messenger:
    def __init__(self, token=os.getenv("DD_ACCESS_TOKEN"), secret=os.getenv("DD_SECRET")):
        self.timestamp = str(round(time.time() * 1000))
        self.URL = "https://oapi.dingtalk.com/robot/send"
        self.headers = {'Content-Type': 'application/json'}
        secret = secret
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(self.timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        self.sign = quote_plus(base64.b64encode(hmac_code))
        self.params = {'access_token': token, "sign": self.sign}

    def send_text(self, content):
        """
        发送文本
        @param content: str, 文本内容
        """
        data = {
            "msgtype": "text",
            "text": {"content": content}
        }

        self.params["timestamp"] = self.timestamp
        return requests.post(
            url=self.URL,
            data=json.dumps(data),
            params=self.params,
            headers=self.headers
        )


if __name__ == "__main__":
    m = Messenger(
        token="2f025d31f1f189e6f3f0d2bbcc1ffde903e441a7807beec9e8d225260fc30b44",
        secret="SEC147c94b837e2ae5fa2ba4bbb8cd752a0679fde4ffd54330c8ae0ec42b9ba45c3"
    )
    m.send_text("")
