from datetime import datetime, timedelta

from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import PeopleToMessage, Admin, PeopleToBans, YellowLeaf
from user.serializers import PeopleToMessageSerializer


# ДОБАВДЕНИЕ ЗАПИСИ, ЧТО ЧЕЛОВЕК НАПИСАЛ СООБЩЕНИЕ
class AddPeopleToMessageAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PeopleToMessageSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        qs = PeopleToMessage.objects.filter(people__id=request.data.get('people'))
        if qs.exists():
            return Response({'message': 'Такой пользователь уже писал сообщение'}, status=status.HTTP_200_OK)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ОБНОВЛЕНИЕ ЗАПИСИ, ЧТО ЧЕЛОВЕК НАПИСАЛ СООБЩЕНИЕ
class UpdatePeopleToMessageAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, people_id):
        person = PeopleToMessage.objects.get(people__id=people_id)
        serializer = PeopleToMessageSerializer(person, data={
            'people': people_id,
            **request.data
        })
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)


# ПИСАЛ ЛИ ЧЕЛОВЕК СООБЩЕНИЯ
class IsExistsPeopleToMessageAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, people_id):
        people_list = PeopleToMessage.objects.filter(people__id=people_id)
        return Response({"is_exists": len(people_list) > 0}, status=status.HTTP_200_OK)


# ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ В yellow_place, ЕСЛИ В ТЕЧЕНИИ :days НЕ БЫЛ АКТИВЕН ПОЛЬЗОВАТЕЛЬ
class AutoBanTimeAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request):
        days = request.data.get('days', None)
        if days is None:
            return HttpResponse("Invalid 'days' parameter")
        days_ago = datetime.now() - timedelta(days=days)
        qs = PeopleToMessage.objects.filter(created_at__gte=days_ago)

        new_banned_user_list = []
        # Баним каждого пользователя, если он не админ
        for user_to_ban in qs:
            user = user_to_ban.people

            # Проверяем, не является ли пользователь админом
            if not Admin.objects.filter(people=user).exists():
                # Создаем запись в таблице PeopleToBans
                new_banned_user = YellowLeaf.objects.create(people=user, created_at=datetime.now())
                new_banned_user_list.append(new_banned_user.id)
        return Response(new_banned_user_list, status=status.HTTP_200_OK)


# ПОЛУЧЕНИЕ ВСЕХ TG ЧАТОВ
class UniqueChatAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        unique_chats = PeopleToMessage.objects.values_list('chat', flat=True).distinct()
        return Response({'chats': unique_chats}, status=status.HTTP_200_OK)