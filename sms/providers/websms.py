__author__ = 'vapnik'
from sms.sender import Sender
import urllib.request


class WebSms(Sender):
    provider = 'websms'
    request_url = 'http://cab.websms.ru//http_in5.asp?'

    def sendrequest(self):
        self.fill_secure_data(['login', 'password'])
        link = self.request_url
        params = {'http_username': self.login, 'http_password': self.password, 'message': self.get_key_for_sms(),
                  'phone_list': self.get_phone()}
        return self.http_request(link, params)
