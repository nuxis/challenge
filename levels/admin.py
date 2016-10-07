from levels.models import Level
from django.contrib import admin

class LevelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'points', 'required_points']

admin.site.register(Level, LevelAdmin)
