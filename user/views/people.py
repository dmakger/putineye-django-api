from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import People, PeopleToBans, OldDataPeople
from user.serializers import PeopleSerializer
from user.service.is_valid_user import BanHelper


# ВСЕ ПОЛЬЗОВАТЕЛИ
class AllPeopleAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        days = request.data.get('days', None)
        if days is not None:
            days_ago = datetime.now() - timedelta(days=days)
            people = People.objects.filter(created_at__gte=days_ago)
        else:
            people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)


# СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ
class AddPersonAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        peoples = People.objects.filter(telegram_id=request.data.get('telegram_id'))
        if len(peoples) > 0:
            return Response({
                'message': 'Такой пользователь существует',
                'id': peoples[0].id,
            }, status=status.HTTP_200_OK)

        serializer.save()
        helper = BanHelper()
        is_valid = helper.is_validated_user(serializer.data.get('phone', None))

        if not is_valid:
            default_ban = helper.get_unfriendly_country()
            PeopleToBans.objects.create(people=serializer.instance, ban=default_ban)

        return Response({'is_valid': is_valid,**serializer.data}, status=status.HTTP_201_CREATED)


# ОБНОВЛЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
class UpdatePersonAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        print(request.data)
        person = get_object_or_404(People, id=pk)
        serializer = PeopleSerializer(person, data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            old_data = OldDataPeople(
                fio_old=person.fio,
                telegram_id_old=person.telegram_id,
                telegram_name_old=person.telegram_name,
                phone_old=person.phone,
                created_at_old=person.created_at,
                people=person,
            )
            old_data.save()

            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ПОЛУЧЕНИЕ ПОЛЬЗОВАТЕЛЯ
class GetDetailPeopleAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        qs = People.objects.filter(**request.data)
        print(request.data)
        print(qs)
        if len(request.data) == 0 or len(qs) == 0:
            return Response({'message': 'Такого пользователя не существует'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PeopleSerializer(qs[0])
        return Response(serializer.data)


# СУЩЕСТВУЕТ ЛИ ЧЕЛОВЕК
class IsExistsPeopleAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        people_list = People.objects.filter(**request.data)
        people_id = None
        if len(people_list) > 0:
            people_id = people_list[0].id
        return Response({
            "is_exists": len(people_list) > 0,
            "id": people_id,
        }, status=status.HTTP_200_OK)

