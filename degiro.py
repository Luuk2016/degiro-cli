import requests
import json
loginURL = 'https://trader.degiro.nl/login/secure/login'
clientURL = 'https://trader.degiro.nl/pa/secure/client'

class DeGiro:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def auth(self):
        payload = {
            'username': self.email,
            'password': self.password,
            'isPassCodeReset': False,
            'isRedirectToMobile': False
        }
        header = {'content-type': 'application/json'}

        r = requests.post(loginURL, headers=header, data=payload)
        result = r.json()

        return result['sessionId']