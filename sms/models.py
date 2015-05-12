from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OneSMS(models.Model):
    send_time = models.DateTimeField()
    receive_time = models.DateTimeField(blank=True, null=True)
    provider = models.ForeignKey(Provider)

    def __str__(self):
        return self.provider + ' ' + self.id