__author__ = 'vapnik'
from datetime import datetime, timedelta
from sms.models import Provider, OneSMS


class Updater:
    @staticmethod
    def calc_deliver_time(begin, end):
        return (end - begin).seconds

    @staticmethod
    def save_last_time(provider, begin, end):
        provider.last_time = Updater.calc_deliver_time(begin.replace(tzinfo=None), end.replace(tzinfo=None))
        provider.save()

    @staticmethod
    def get_average_time(provider):
        smss = OneSMS.objects.filter(provider=provider)
        count = 0
        sum = 0
        for sms in smss:
            count += 1
            sum += Updater.calc_deliver_time(sms.send_time, sms.receive_time)
        return sum / count

    @staticmethod
    def save_average_time(provider):
        provider.average_time = Updater.get_average_time(provider)
        provider.save()