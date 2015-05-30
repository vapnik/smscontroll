

__author__ = 'vapnik'
from sms.sender import Sender


class SmsRu(Sender):
    provider = 'smsru'
    request_url = 'http://sms.ru/sms/send?'

    def sendrequest(self):
        self.fill_secure_data(['apiKey'])
        link = self.request_url
        params = {'api_id': self.apiKey, 'text': self.get_key_for_sms(), 'to': self.get_phone()}
        return self.http_request(link, params)