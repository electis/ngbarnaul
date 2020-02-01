from django.contrib import admin
from django.apps import apps
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from solo.admin import SingletonModelAdmin
from apps.core import models


@admin.register(models.Setting)
class SettingsAdmin(SingletonModelAdmin, DynamicArrayMixin):
    pass

@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass

apps_models = apps.get_models()
for model in apps_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
