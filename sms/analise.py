__author__ = 'vapnik'
from datetime import datetime, timedelta
from sms.models import Provider


class Updater:
    @staticmethod
    def calc_deliver_time(begin, end):
        return (end - begin).seconds

    @staticmethod
    def save_last_time(provider, begin, end):
        provider.last_time = Updater.calc_deliver_time(begin.replace(tzinfo=None), end.replace(tzinfo=None))
        provider.save()