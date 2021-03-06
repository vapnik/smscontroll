from sms.models import Provider, OneSMS
from datetime import datetime
from django.utils.crypto import get_random_string
import urllib
from urllib.parse import urlencode


class Sender:
    provider = 'abstract'
    sms_id = False
    phone = False
    login = False
    password = False
    apiKey = False
    key = False

    def __init__(self, phone=False, provider=False):
        if phone:
            self.setPhone(phone)
        if provider:
            self.setprovider(provider)

    def get_key_for_sms(self):
        return "SMSTEST#" + self.key

    def setPhone(self, phone):
        self.phone = phone

    def get_phone(self):
        phone = self.check(self.phone)
        if phone:
            return phone
        else:
            raise PhoneError(phone)

    def setprovider(self, provider):
        self.provider = provider

    def make_key(self):
        self.key = get_random_string(12)

    def send(self):
        self.make_key()
        result = self.sendrequest()
        self.save()
        return result

    def sendrequest(self):
        pass

    def fill_secure_data(self, fields):
        provider = self.getProvider()
        for index in range(len(fields)):
            if getattr(provider, fields[index]):
                setattr(self, fields[index], getattr(provider, fields[index]))
            else:
                raise SecureFieldDoesNotExist(provider.name, fields[index])

    @staticmethod
    def check(phone):
        if len(phone) < 10:
            return False
        else:
            return phone

    @staticmethod
    def http_request(link, params):
        link += urlencode(params)
        response = urllib.request.urlopen(link)
        response = response.read().decode(encoding='utf-8')
        response.encode('UTF-8')
        return response

    def save(self):
        provider = self.getProvider()
        sms = OneSMS(provider=provider, send_time=datetime.now(), key=self.key)
        sms.save()
        return sms.id

    def getProvider(self):
        provider_name = self.provider
        try:
            provider = Provider.objects.get(name=provider_name)
        except Provider.DoesNotExist:
            provider = Provider(name=self.provider)
            provider.save()
        return provider


class SendError(Exception):
    phone = ''
    provider = ''

    def __init__(self, phone, provider):
        self.phone = phone
        self.provider = provider


class PhoneError(Exception):
    def __init__(self, phone):
        self.phone = phone


class SecureFieldDoesNotExist(Exception):
    def __init__(self, provider, field):
        self.provider = provider
        self.field = field