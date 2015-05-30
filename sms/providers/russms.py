__author__ = 'vapnik'
from sms.sender import Sender
import urllib.request


class RusSMS(Sender):
    provider = 'rus-sms'
    request_url = 'http://cabinet.rus-sms.ru/lcabApi/sendSms.php'

    def sendrequest(self):
        self.fill_secure_data(['login', 'password'])
        link = self.request_url + '?login=' + self.login + '&password=' + self.password + '&txt='
        link += self.get_key_for_sms() + '&to=' + self.get_phone()
        response = urllib.request.urlopen(link)
        response = response.read().decode(encoding='utf-8')
        response.encode('UTF-8')
        return response