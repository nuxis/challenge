from levels.models import Level
from django.contrib import admin

class LevelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'points', 'point_requirement']

admin.site.register(Level, LevelAdmin)
