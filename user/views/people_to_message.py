from datetime import datetime, timedelta

from django.db.models import QuerySet
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import PeopleToMessage, Admin, PeopleToBans, YellowLeaf
from user.serializers import PeopleToMessageSerializer
from user.service.ban import BanVariables, BanHelper


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
        # Получение сообщений до "days_ago"
        qs: QuerySet[PeopleToMessage] = PeopleToMessage.objects.filter(created_at__lte=days_ago)
        # Исключение пользователей, которые являются админами
        qs_n = qs.exclude(people__admin__isnull=False)
        # Получение всех пользователей которые уже находятся в "Желтом списке"
        existing_users = YellowLeaf.objects.values('people')
        # Исключение всех пользователей которые уже находятся в "Желтом списке"
        not_existing_users: QuerySet[PeopleToMessage] = qs_n.exclude(people__in=existing_users)
        new_banned_user_list = []
        ban_helper = BanHelper()
        for user in not_existing_users:
            new_banned_user = YellowLeaf.objects.create(people=user.people, ban=ban_helper.inaction())
            new_banned_user_list.append(new_banned_user.id)
        return Response(new_banned_user_list, status=status.HTTP_200_OK)


# ПОЛУЧЕНИЕ ВСЕХ TG ЧАТОВ
class UniqueChatAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        unique_chats = PeopleToMessage.objects.values_list('chat', flat=True).distinct()
        return Response({'chats': unique_chats}, status=status.HTTP_200_OK)