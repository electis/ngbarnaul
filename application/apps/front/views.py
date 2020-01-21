import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

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
        }
        id = request.POST.get('id')
        if id in methods.keys():
            try:
                data = json.loads(request.POST['data'])
            except:
                return HttpResponse(status=400)
            print('Send email', methods[id], data)
            return HttpResponse()
        return HttpResponse(status=400)
