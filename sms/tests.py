from django.test import TestCase
from sms.sender import Sender, SecureFieldDoesNotExist
from django.utils.crypto import get_random_string
from sms.models import Provider, OneSMS


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