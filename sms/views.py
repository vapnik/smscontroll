from django.shortcuts import render
from django.http import HttpResponse
from sms.russms import RusSMS


def russms(request):
    sms = RusSMS(phone=request.GET.get('phone'))
    response = 'send to ' + request.GET.get('phone') + '<br>'
    response += sms.send()
    return HttpResponse(response)