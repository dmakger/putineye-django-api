from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views.admin import AllAdminAPIView, AddAdminAPIView, UpdateAdminAPIView, RemoveAdminView, IsAdminAPIView
from user.views.ban import AllPeopleToBanAPIView, AddPeopleToBanAPIView, UpdatePeopleToBanAPIView, \
    RemovePeopleToBanView, IsBannedPeopleToBanAPIView
from user.views.people import AllPeopleAPIView, AddPersonAPIView, UpdatePersonAPIView, GetDetailPeopleAPIView, \
    IsExistsPeopleAPIView
from user.views.people_to_message import AddPeopleToMessageAPIView, UpdatePeopleToMessageAPIView, \
    IsExistsPeopleToMessageAPIView, AutoBanTimeAPIView, UniqueChatAPIView
from user.views.yellow_leaf import AllYellowLeafAPIView, AddYellowLeafAPIView, UpdateYellowLeafAPIView, \
    RemoveYellowLeafView, IsExistsYellowLeafAPIView, GetDetailYellowLeafAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # PEOPLE
    path('people/all/', AllPeopleAPIView.as_view(), name='all_people_api'),
    path('people/get/', GetDetailPeopleAPIView.as_view(), name='get_people_api'),
    path('people/add/', AddPersonAPIView.as_view(), name='add_person_api'),
    path('people/update/<int:pk>/', UpdatePersonAPIView.as_view(), name='update_person_api'),
    path('people/is_exists/', IsExistsPeopleAPIView.as_view(), name='is_exists_person_api'),

    # ADMIN
    path('admin/all/', AllAdminAPIView.as_view(), name='all_admins_api'),
    path('admin/add/', AddAdminAPIView.as_view(), name='add_admin_api'),
    path('admin/update/<int:people_id>/', UpdateAdminAPIView.as_view(), name='update_admin_api'),
    path('admin/remove/<int:people_id>/', RemoveAdminView.as_view(), name='remove_admin_api'),
    path('admin/is_admin/<int:people_id>/', IsAdminAPIView.as_view(), name='is_admin_api'),

    # BAN
    path('ban/all/', AllPeopleToBanAPIView.as_view(), name='all_ban_api'),
    path('ban/add/', AddPeopleToBanAPIView.as_view(), name='add_ban_api'),
    path('ban/update/<int:people_id>/', UpdatePeopleToBanAPIView.as_view(), name='update_ban_api'),
    path('ban/remove/<int:people_id>/', RemovePeopleToBanView.as_view(), name='remove_ban_api'),
    path('ban/is_banned/<int:people_id>/', IsBannedPeopleToBanAPIView.as_view(), name='is_banned_user_api'),

    # YELLOW LEAF
    path('yellow_leaf/all/', AllYellowLeafAPIView.as_view(), name='all_yellow_leaf_api'),
    path('yellow_leaf/get/', GetDetailYellowLeafAPIView.as_view(), name='get_yellow_leaf_api'),
    path('yellow_leaf/add/', AddYellowLeafAPIView.as_view(), name='add_yellow_leaf_api'),
    path('yellow_leaf/update/<int:people_id>/', UpdateYellowLeafAPIView.as_view(), name='update_yellow_leaf_api'),
    path('yellow_leaf/remove/<int:people_id>/', RemoveYellowLeafView.as_view(), name='remove_yellow_leaf_api'),
    path('yellow_leaf/is_exists/<int:people_id>/', IsExistsYellowLeafAPIView.as_view(), name='is_exists_user_in_yellow_leaf_api'),

    # PEOPLE TO MESSAGE
    path('message/add/', AddPeopleToMessageAPIView.as_view(), name='add_people_to_message_api'),
    path('message/update/<int:people_id>/', UpdatePeopleToMessageAPIView.as_view(),
         name='update_people_to_message_api'),
    path('message/is_exists/<int:people_id>/', IsExistsPeopleToMessageAPIView.as_view(),
         name='is_exists_people_to_message_api'),
    path('message/auto_ban/', AutoBanTimeAPIView.as_view(), name='auto_ban_api'),
    path('message/tg_chat/', UniqueChatAPIView.as_view(), name='get_tg_chat_api'),
]
