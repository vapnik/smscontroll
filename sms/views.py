from django.shortcuts import render
from django.http import HttpResponse
from sms.russms import RusSMS


def russms(request):
    sms = RusSMS()

    response = 'send to ' + request.GET.get('phone') + '<br>'
    response += sms.sendrequest(request.GET.get('phone'))
    return HttpResponse(response)