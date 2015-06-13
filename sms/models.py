from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    apiKey = models.CharField(max_length=255, blank=True, null=True)
    last_time = models.IntegerField(blank=True, null=True)
    optimal_rules = models.BooleanField(default=False)
    average_time = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class OneSMS(models.Model):
    send_time = models.DateTimeField()
    receive_time = models.DateTimeField(blank=True, null=True)
    provider = models.ForeignKey(Provider)
    key = models.CharField(max_length=12)

    def __str__(self):
        return self.provider.__str__() + ' ' + self.key