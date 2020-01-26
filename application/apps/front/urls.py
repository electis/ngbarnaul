from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('ajax/', views.Ajax.as_view()),
    re_path(r'^'+'|^'.join(views.card_urls), views.Card.as_view()),
    re_path(r'^'+'|^'.join(views.tab_urls), views.Tab.as_view()),
]
