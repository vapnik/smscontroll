from django.test import TestCase
from sms.sender import Sender, SecureFieldDoesNotExist
from django.utils.crypto import get_random_string
from sms.models import Provider, OneSMS
from sms.reciever import Receiver, InvalidKey
from datetime import datetime


class SenderTest(TestCase):
    def setUp(self):
        self.sender = Sender()

    def test_check(self):
        self.assertTrue(self.sender.check('+7(918)5080501'))
        self.assertTrue(self.sender.check('+7(918)508-05-01'))
        self.assertTrue(self.sender.check('7(918)508-05-01'))
        self.assertFalse(self.sender.check('1'))

    def test_provider_creation(self):
        provider_name = get_random_string(length=10)
        self.sender.setprovider(provider_name)
        self.sender.getProvider()
        provider = Provider.objects.get(name=provider_name)
        self.assertTrue(provider.name == provider_name)

    def test_save_sms(self):
        id = self.sender.save()
        sms = OneSMS(id=id)

    def test_secure_data(self):
        fields = ['login', 'password']
        try:
            self.sender.fill_secure_data(fields)
            self.assertTrue(False)
        except SecureFieldDoesNotExist:
            pass
        fields = ['name', 'login', 'password', 'apiKey']
        values = []
        for i in range(len(fields)):
            values.append(get_random_string())
        provider = Provider(name=values[0], login=values[1], password=values[2], apiKey=values[3])
        provider.save()
        self.sender.setprovider(values[0])
        del fields[0]
        self.sender.fill_secure_data(fields)
        self.assertEqual(values[1], self.sender.login)
        self.assertEqual(values[2], self.sender.password)
        self.assertEqual(values[3], self.sender.apiKey)


class ReceiverTest(TestCase):
    def setUp(self):
        self.reciever = Receiver()

    def test_check_key(self):
        invalid_key = get_random_string(10)
        valid_key = get_random_string(12)
        try:
            self.reciever.check_key(invalid_key)
            self.assertTrue(False)
        except InvalidKey:
            pass
        self.assertEqual(self.reciever.check_key(valid_key), valid_key)

    def test_find_sms(self):

        valid_key = get_random_string(12)
        invalid_key = get_random_string(12)
        TestTools.make_random_sms(valid_key)
        self.reciever.set_key(valid_key)
        self.reciever.find_sms()
        self.assertEqual(self.reciever.sms.key, valid_key)


class TestTools:
    @staticmethod
    def make_random_provider():
        fields = ['name', 'link', 'apiKey', 'login', 'password']
        provider_fields = {}
        while len(fields) > 0:
            provider_fields[fields.pop(0)] = get_random_string()
        provider = Provider(**provider_fields)
        provider.save()
        return provider

    @staticmethod
    def make_random_sms(key=False):
        if not key:
            key = get_random_string(12)
        fields = {'send_time': datetime.now(), 'provider': TestTools.make_random_provider(),
                  'key': key}
        sms = OneSMS(**fields)
        sms.save()
        return sms


class TestTestTools(TestCase):
    def test_make_provider(self):
        provider = TestTools.make_random_provider()
        fields = ['name', 'link', 'apiKey', 'login', 'password']
        db_provider = Provider.objects.get(id=provider.id)
        for key in fields:
            self.assertEqual(len(getattr(db_provider, key)), 12)

    def test_make_sms(self):
        sms = TestTools.make_random_sms()
        db_sms = OneSMS.objects.get(id=sms.id)
        self.assertEqual(len(db_sms.key), 12)

        key = get_random_string(12)
        sms = TestTools.make_random_sms(key)
        db_sms = OneSMS.objects.get(id=sms.id)
        self.assertEqual(db_sms.key, key)