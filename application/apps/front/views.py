import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings

from apps.core import models

card_urls = ('healing', 'social', 'psycholog', 'finance')


class Index(View):
    def get(self, request):
        context = {
            'title': 'Главная',
            'ministers': models.Minister.objects.all(),
            'cards': models.Card.objects.all(),
        }
        # context['settings'] = models.Setting.objects.first()
        # context['contact'] = models.Contact.objects.first()
        # context['navbar'] = models.Navbar.objects.all()
        # context['banner'] = models.Banner.objects.all()
        # context['counter'] = models.Counter.objects.all()
        # context['card'] = models.Card.objects.all()
        # context['review'] = models.Review.objects.all()
        # context['team'] = models.Team.objects.all()
        return render(request, 'index.html', context)


class Card(View):
    def get(self, request):
        card = models.Card.objects.filter(url=request.path.replace('/', '')).first()
        if not card:
            return HttpResponseRedirect('/')
        context = {
            'title': card.text_top,
            'ministers': models.Minister.objects.all(),
        }
        # context['settings'] = models.Setting.objects.first()
        # context['contact'] = models.Contact.objects.first()
        # context['navbar'] = models.Navbar.objects.all()
        # context['banner'] = models.Banner.objects.all()
        # context['counter'] = models.Counter.objects.all()
        # context['card'] = models.Card.objects.all()
        # context['review'] = models.Review.objects.all()
        # context['team'] = models.Team.objects.all()
        return render(request, f'{card.url}.html', context)


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
            mail = EmailMultiAlternatives(methods[id], data, settings.EMAIL_HOST_USER, email)
            mail.content_subtype = "html"
            try:
                mail.send(fail_silently=False)
            except Exception as Ex:
                print(Ex)
            return HttpResponse()
        else:
            print('Method unknown: ', id)
        return HttpResponse(status=400)
