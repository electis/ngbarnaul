import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings

from apps.core import models

# card_urls = ('healing', 'social', 'psycholog', 'finance')
card_urls = models.Card.objects.values_list('url', flat=True)
tab_urls = models.Tab.objects.values_list('url', flat=True)


class Index(View):
    def get(self, request):
        context = {
            'title': 'Главная',
            'ministers': models.Minister.objects.all(),
            'cards': models.Card.objects.all(),
            'tabs': models.Tab.objects.all(),
        }
        return render(request, 'index.html', context)


class Card(View):
    def get(self, request):
        card = models.Card.objects.filter(url=request.path.replace('/', '')).first()
        if not card:
            return HttpResponseRedirect('/')
        context = {
            'title': card.name,
            'cards': models.Card.objects.all(),
            'tabs': models.Tab.objects.all(),
        }
        return render(request, f'{card.url}.html', context)


class Tab(View):
    def get(self, request):
        tab = models.Tab.objects.filter(url=request.path.replace('/', '')).first()
        if not tab:
            return HttpResponseRedirect('/')
        context = {
            'title': tab.name,
            'cards': models.Card.objects.all(),
            'tabs': models.Tab.objects.all(),
        }
        return render(request, f'{tab.url}.html', context)


class Ajax(View):
    def post(self, request):
        methods = {
            'form-footer': 'Обратная связь',
            'form-healing': 'Исцеление - консультация',
            'form-healing-modal': 'Исцеление - молитва',
            'form-social': 'Социальная помощь',
            'form-psycholog': 'Психолог - записаться',
            'form-psycholog-modal': 'Психолог - видеовыпуск',
            'form-finance': 'Финансы - записаться',
            'form-finance-modal': 'Финансы - книга',
        }
        id = request.POST.get('id')
        if id in methods.keys():
            try:
                data = json.loads(request.POST['data'])
            except:
                return HttpResponse(status=400)
            email = ['andrey@ngbarnaul.ru']
            print('Send email', methods[id], data)
            html = str('<br>'.join([f"{d.get('name')}: {d.get('value')}" for d in data]))
            mail = EmailMultiAlternatives(methods[id], html, settings.EMAIL_HOST_USER, email)
            mail.content_subtype = "html"
            try:
                mail.send(fail_silently=False)
            except Exception as Ex:
                print(Ex)
                return HttpResponse(status=400)
            return HttpResponse()
        else:
            print('Method unknown: ', id)
        return HttpResponse(status=400)
