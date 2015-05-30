__author__ = 'vapnik'

from sms.sender import Sender


class SmsIntel(Sender):
    provider = 'smsintel'
    request_url = 'https://lcab.smsintel.ru/lcabApi/sendSms.php?'

    def sendrequest(self):
        self.fill_secure_data(['login', 'password'])
        params = {'login': self.login, 'password': self.password, 'txt': self.get_key_for_sms(), 'to': self.get_phone()}
        return self.http_request(self.request_url, params)