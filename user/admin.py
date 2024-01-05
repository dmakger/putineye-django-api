from django.contrib import admin

#  Пользователь
from user.models import PeopleToBans, People, Admin, Ban, PeopleToMessage, YellowLeaf, OldDataPeople


class PeopleAdmin(admin.ModelAdmin):
    list_display = ['fio', 'phone', 'telegram_id', 'telegram_name', 'created_at']


class OldDataPeopleAdmin(admin.ModelAdmin):
    list_display = ['fio_old', 'telegram_id_old', 'telegram_name_old', 'phone_old', 'created_at_old', 'people', 'changed_at']


class PeopleToMessageAdmin(admin.ModelAdmin):
    list_display = ['people', 'chat', 'created_at']


#  Админ
class AdminAdmin(admin.ModelAdmin):
    list_display = ['people', 'created_at']


#  Виды баннов
class BanAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


#  Забаненный пользователь
class PeopleToBansAdmin(admin.ModelAdmin):
    list_display = ['people', 'ban', 'created_at']


#  Желтый список
class YellowLeafAdmin(admin.ModelAdmin):
    list_display = ['people', 'ban', 'created_at']


admin.site.register(People, PeopleAdmin)
admin.site.register(OldDataPeople, OldDataPeopleAdmin)
admin.site.register(PeopleToMessage, PeopleToMessageAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Ban, BanAdmin)
admin.site.register(PeopleToBans, PeopleToBansAdmin)
admin.site.register(YellowLeaf, YellowLeafAdmin)
