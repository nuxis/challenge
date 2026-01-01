from levels.models import Level, Attempt
from django.contrib import admin


class LevelAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description", "points", "required_points"]


admin.site.register(Level, LevelAdmin)


class AttemptAdmin(admin.ModelAdmin):
    list_display = ["user", "level", "time", "correct"]
    search_fields = ("user__username",)


admin.site.register(Attempt, AttemptAdmin)
