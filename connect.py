import random
import string

import requests
from urllib.parse import unquote

CLIENT_ID = '98v2m70zi0i8lkgqzy8pwed0kqmztz'
API = 'https://id.twitch.tv'

class Twitch():
    """Connect to Twitch.tv"""
    def __init__(self):
        self.session = requests.Session()

    def authorize(self):
        def parms(headers: dict):
            """  """
            for key, value in headers.items():
                yield f'{key}={value}'
        def token_to_dict(token: str) -> dict:
            """ """
            params = token.split('&')
            param_dict = {}
            for param in params:
                key, value = (param.replace('&', '')).split('=')
                param_dict[key] = value
            return param_dict
        endpoint = '/oauth2/authorize?'
        random_token = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(32))
        headers = {
            'response_type': 'token',
            'client_id': CLIENT_ID,
            'redirect_uri': 'http://localhost',
            'scope': 'user:edit:broadcast',
            'state': random_token
        }
        print('請點擊以下網址授權本軟體透過 Twitch API v5 修改您的直播台遊戲名稱，授權後等待網頁跳轉並複製網址貼上即可。')
        print(API + endpoint + '&'.join(parms(headers)))
        try:
            token = unquote(input('等待輸入: ')).split('#')[1]
        except Exception as error:
            print(f'{error.__class__.__name__}: {error.__str__}')
        print(token_to_dict(token))

if __name__ == '__main__':
    test = Twitch()
    test.authorize()

