from django.http import HttpResponse
from sms.providers.russms import RusSMS
from sms.providers.smsru import SmsRu
from sms.providers.smsintel import SmsIntel
from sms.providers.websms import WebSms
from sms.reciever import Receiver


def russms(request):
    sms = RusSMS(phone=request.GET.get('phone'))
    response = 'send to ' + request.GET.get('phone') + '<br>'
    response += sms.send()
    return HttpResponse(response)


def smsru(request):
    sms = SmsRu(phone=request.GET.get('phone'))
    response = 'send to ' + request.GET.get('phone') + '<br>'
    response += sms.send()
    return HttpResponse(response)


def smsintel(request):
    sms = SmsIntel(phone=request.GET.get('phone'))
    response = 'send to ' + request.GET.get('phone') + '<br>'
    response += sms.send()
    return HttpResponse(response)


def websms(request):
    sms = WebSms(phone=request.GET.get('phone'))
    response = 'send to ' + request.GET.get('phone') + '<br>'
    response += sms.send()
    return HttpResponse(response)


def receive(request):
    key = request.GET.get('key')
    Receiver(key)
    return HttpResponse('Код сохранен')

