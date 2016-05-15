from core.models import Config
from solo.admin import SingletonModelAdmin
from django.contrib import admin

admin.site.register(Config, SingletonModelAdmin)
