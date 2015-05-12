from sms.models import Provider, OneSMS
from datetime import datetime
from django.utils.crypto import get_random_string


class Sender:
    provider = 'abstract'
    sms_id = False
    phone = False
    login = False
    password = False
    api_key = False
    key = False

    def __init__(self, phone=False, provider=False):
        if phone:
            self.setPhone(phone)
        if provider:
            self.setprovider(provider)

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

    def send(self):
        self.key = get_random_string(12)
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