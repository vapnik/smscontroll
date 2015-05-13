__author__ = 'vapnik'
from sms.models import OneSMS


class Receiver():
    key = False
    sms = False

    def __init__(self, key=False):
        if key:
            self.set_key(key)

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
                raise KeyDoesNotExist(self.key)
        else:
            raise InvalidKey(self.key)
        if self.sms.receive_time:
            raise self.HasBeenReceived(self.key)

    class HasBeenReceived(Exception):
        def __init__(self, key):
            self.key = key


class InvalidKey(Exception):
    def __init__(self, key):
        self.key = key


class KeyDoesNotExist(Exception):
    def __init__(self, key):
        self.key = key