from django.urls import path
from application.front import views

urlpatterns = [
    path('', views.Index.as_view()),
]
