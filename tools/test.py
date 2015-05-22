__author__ = 'vapnik'

from tools.logger import BaseLogger
from django.test import TestCase
from django.utils.crypto import get_random_string

class LoggerTest(TestCase):
    def setUp(self):
        self.logger = BaseLogger()

    def test_add(self):
        message = get_random_string()
        self.logger.log(message)

    def test_read(self):
        message = get_random_string()
        self.logger.log(message)
        self.assertEqual(message, self.logger.get_last())