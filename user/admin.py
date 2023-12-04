from django.contrib import admin


#  Пользователь
from user.models import PeopleToBans, People, Admin, Ban


class PeopleAdmin(admin.ModelAdmin):
    list_display = ['fio', 'phone', 'telegram_id', 'telegram_name', 'created_at']


#  Админ
class AdminAdmin(admin.ModelAdmin):
    list_display = ['people', 'created_at']


#  Виды баннов
class BanAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


#  Забаненный пользователь
class PeopleToBansAdmin(admin.ModelAdmin):
    list_display = ['people', 'ban', 'created_at']


admin.site.register(People, PeopleAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Ban, BanAdmin)
admin.site.register(PeopleToBans, PeopleToBansAdmin)
