from django.shortcuts import render
from django.views import View

from application.core import models


class Index(View):
    def get(self, request):
        context = {}
        context['title'] = 'Главная'
        # context['settings'] = models.Setting.objects.first()
        # context['contact'] = models.Contact.objects.first()
        # context['navbar'] = models.Navbar.objects.all()
        # context['banner'] = models.Banner.objects.all()
        # context['counter'] = models.Counter.objects.all()
        # context['card'] = models.Card.objects.all()
        # context['review'] = models.Review.objects.all()
        # context['team'] = models.Team.objects.all()
        context['ministers'] = models.Minister.objects.all()
        return render(request, 'index.html', context)
