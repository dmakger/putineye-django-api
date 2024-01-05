from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from tg.models import Settings
from tg.serializers import SettingsSerializer


# ПОЛУЧЕНИЕ "ПРИВЕТСТВЕННОГО ТЕКСТА"
class WelcomeTextAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        settings = get_object_or_404(Settings, id=1)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)


# ПОЛУЧЕНИЕ "Бан-текста"
class BanTextAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        settings = get_object_or_404(Settings, id=2)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)


# ПОЛУЧЕНИЕ "Текст вступления в группу"
class JoiningGroupAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        settings = get_object_or_404(Settings, id=3)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)


# ПОЛУЧЕНИЕ "Текст в процессе рассмотрения"
class ProcessTextAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        settings = get_object_or_404(Settings, id=4)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)

