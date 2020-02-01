import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
from django.core.validators import validate_email

from apps.core import models

# card_urls = ('healing', 'social', 'psycholog', 'finance')
card_urls = models.Card.objects.values_list('url', flat=True)
tab_urls = models.Tab.objects.values_list('url', flat=True)


class Index(View):
    def get(self, request):
        context = {
            'title': 'Главная',
            'ministers': models.Minister.objects.filter(active=True),
            'cards': models.Card.objects.all(),
            'tabs': models.Tab.objects.all(),
            'settings': models.Setting.get_solo(),
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
    status = 200
    text = 'OK'

    def post(self, request):
        methods = {
            'form-subscribe': 'Главная - подписка',
            'form-footer': 'Обратная связь',
            'form-healing': 'Исцеление - консультация',
            'form-healing-modal': 'Исцеление - молитва',
            'form-social': 'Социальная помощь',
            'form-psycholog': 'Психолог - записаться',
            'form-psycholog-modal': 'Психолог - видеовыпуск',
            'form-finance': 'Финансы - записаться',
            'form-finance-modal': 'Финансы - книга',
        }
        method = request.POST.get('id')
        if method in methods.keys():
            try:
                data_list = json.loads(request.POST['data'])
                data_dict = {item['name_attr'].lower(): item.get('value')
                             for item in data_list if item.get('name_attr').lower() in models.SendedForm.fields}
            except:
                self.text = 'Ошибка в данных, сообщите администратору'
                self.status = 415
            else:
                if method in models.Subscriber.methods:
                    try:
                        validate_email(data_dict.get('email'))
                    except:
                        self.text = 'Неправильный Email'
                        self.status = 415
                    else:
                        models.Subscriber.objects.get_or_create(method=method, email=data_dict.get('email'))
                if method in models.SendedForm.methods:
                    sended_form = models.SendedForm.objects.create(method=method, **data_dict)
                    html = str('<br>'.join([f"{d.get('name')}: {d.get('value')}" for d in data_list]))
                    mail = EmailMultiAlternatives(methods[method], html, settings.EMAIL_HOST_USER, models.SendedForm.emails)
                    mail.content_subtype = "html"
                    try:
                        mail.send(fail_silently=False)
                    except Exception as Ex:
                        self.text = f'Ошибка отправки сообщения {Ex}'
                        self.status = 404
                    else:
                        sended_form.sended = True
                        sended_form.save()
        else:
            self.text = f'Method unknown: {method}'
            self.status = 405
        return HttpResponse(status=self.status, content=self.text)
