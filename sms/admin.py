from django.contrib import admin
from sms.models import Provider, OneSMS

admin.site.register(Provider)
admin.site.register(OneSMS)