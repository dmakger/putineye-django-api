from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import PeopleToBans
from user.serializers import PeopleToBanSerializer, PeopleToBanFuncSerializer


# ВСЕ ЗАБАННЕНЫЕ
class AllPeopleToBanAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        days = request.data.get('days', None)
        if days is not None:
            days_ago = datetime.now() - timedelta(days=days)
            people = PeopleToBans.objects.filter(created_at__gte=days_ago)
        else:
            people = PeopleToBans.objects.all()
        serializer = PeopleToBanSerializer(people, many=True)
        return Response(serializer.data)


# БАН ПОЛЬЗОВАТЕЛЯ
class AddPeopleToBanAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PeopleToBanFuncSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        qs = PeopleToBans.objects.filter(people__id=request.data.get('people'))
        if len(qs) > 0:
            return Response({'message': 'Такой пользователь уже забанен'}, status=status.HTTP_200_OK)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ЭТОТ ПОЛЬЗОВАТЕЛЬ ЯВЛЯЕТСЯ ЛИ ВАЛИДНЫМ
class IsValidPeopleToBanAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, people_id):
        people_list = PeopleToBans.objects.filter(people__id=people_id)
        return Response({"is_valid": len(people_list) == 0}, status=status.HTTP_200_OK)


# ОБНОВЛЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
class UpdatePeopleToBanAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, people_id):
        person = PeopleToBans.objects.get(people__id=people_id)
        serializer = PeopleToBanFuncSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# РАЗБАН
class RemovePeopleToBanView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, people_id):
        try:
            people_to_ban = PeopleToBans.objects.get(people__id=people_id)
        except Exception:
            return Response({"detail": "Пользователь с указанным id не найден"}, status=status.HTTP_404_NOT_FOUND)

        people_to_ban.delete()
        return Response({"detail": "Пользователь успешно разбанен"}, status=status.HTTP_204_NO_CONTENT)
