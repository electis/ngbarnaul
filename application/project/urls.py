from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('adminka/', admin.site.urls),
    path('', include('apps.front.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
