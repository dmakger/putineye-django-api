from django.contrib import admin

from tg.models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


admin.site.register(Settings, SettingsAdmin)
