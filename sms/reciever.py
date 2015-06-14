__author__ = 'vapnik'
from sms.models import OneSMS
from datetime import datetime
from sms.analise import Updater


class Receiver():
    key = False
    sms = False

    def __init__(self, key=False):
        if key:
            self.set_key(key)
            self.find_sms()
            self.save_time()

    @staticmethod
    def check_key(key):
        if len(key) == 12:
            return key
        else:
            raise InvalidKey(key)

    def set_key(self, key):
        self.key = self.check_key(key)

    def find_sms(self):
        if self.key:
            try:
                self.sms = OneSMS.objects.get(key=self.key)
            except OneSMS.DoesNotExist:
                raise self.KeyDoesNotExist(self.key)
        else:
            raise InvalidKey(self.key)

    def save_time(self):
        if not self.sms:
            raise self.SmsDoesNotDefined()
        if self.sms.receive_time:
            raise self.HasBeenReceived(self.key)
        self.sms.receive_time = datetime.now()
        self.sms.save()
        Updater.save_last_time(self.sms.provider, self.sms.receive_time, self.sms.send_time)
        Updater.save_average_time(self.sms.provider)

    class HasBeenReceived(Exception):
        def __init__(self, key):
            self.key = key

    class SmsDoesNotDefined(Exception):
        pass

    class KeyDoesNotExist(Exception):
        def __init__(self, key):
            self.key = key


class InvalidKey(Exception):
    def __init__(self, key):
        self.key = key


