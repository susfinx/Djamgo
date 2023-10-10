from django.shortcuts import render
import random as rd
from django.http import HttpResponse

import logging

from django.utils import timezone

from sem2app.models import Onehed

loger= logging.getLogger(__name__)

def one(request):
    loger.info('One start')
    n = request.GET.get('n', '5')
    answer = rd.choice(['OREL', 'RESHKA']) == 'OREL'
    res_w = Onehed(rest_time=timezone.now(), res=answer)  # Здесь исправлено использование timezone.now()
    res_w.save()
    return HttpResponse(res_w.statistic(n))  # Используйте объект res_w для вызова метода statistic


def two (request):
    loger.info('Two start')
    return HttpResponse(f'Znachenie kubika {rd.randint(1,6)}.')

def tre (request):

    loger.info('tre start')
    return HttpResponse(f'sluchaynoe znachenie ot 0 do 100 - {rd.randint(0,100)}')