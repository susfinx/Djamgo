from django.shortcuts import render
import random as rd
from django.http import HttpResponse
import logging

loger= logging.getLogger(__name__)

def one (request):
    loger.info('One start')
    answer=['OREL', 'RESHKA']

    return HttpResponse(rd.choice(answer))

def two (request):
    loger.info('Two start')
    return HttpResponse(f'Znachenie kubika {rd.randint(1,6)}.')

def tre (request):

    loger.info('tre start')
    return HttpResponse(f'sluchaynoe znachenie ot 0 do 100 - {rd.randint(0,100)}')