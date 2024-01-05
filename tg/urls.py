from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tg.views import WelcomeTextAPIView, BanTextAPIView, JoiningGroupAPIView, ProcessTextAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('text/welcome/', WelcomeTextAPIView.as_view(), name='welcome_text_api'),
    path('text/ban/', BanTextAPIView.as_view(), name='ban_text_api'),
    path('text/joining_group/', JoiningGroupAPIView.as_view(), name='joining_group_text_api'),
    path('text/process/', ProcessTextAPIView.as_view(), name='process_text_api'),
]
