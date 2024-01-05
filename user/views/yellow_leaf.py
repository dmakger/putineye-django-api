# ВСЕ ЗАБАННЕНЫЕ
from datetime import timedelta, datetime

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import YellowLeaf, People, Admin
from user.serializers import YellowLeafSerializer, YellowLeafFuncSerializer


class AllYellowLeafAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        days = request.data.get('days', None)
        if days is not None:
            days_ago = datetime.now() - timedelta(days=days)
            people = YellowLeaf.objects.filter(created_at__gte=days_ago)
        else:
            people = YellowLeaf.objects.all()
        serializer = YellowLeafSerializer(people, many=True)
        return Response(serializer.data)


# ПОЛУЧЕНИЕ ПОЛЬЗОВАТЕЛЯ
class GetDetailYellowLeafAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        qs = People.objects.filter(**request.data)
        if len(qs) == 0:
            return Response({'message': 'Такого пользователя не существует'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = YellowLeafSerializer(qs[0])
        return Response(serializer.data)


# БАН ПОЛЬЗОВАТЕЛЯ
class AddYellowLeafAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = YellowLeafFuncSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        qs = YellowLeaf.objects.filter(people__id=request.data.get('people'))
        if len(qs) > 0:
            return Response({'message': 'Такой пользователь уже находится в желтом листе'}, status=status.HTTP_200_OK)
        serializer.save()

        # Является ли пользователь админом
        people_id = serializer.data.get('people')
        user = People.objects.get(pk=people_id)
        # Проверяем, является ли пользователь админом
        admin_qs = Admin.objects.filter(people=user)
        if admin_qs.exists():
            admin_qs.delete()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ЭТОТ ПОЛЬЗОВАТЕЛЬ ЯВЛЯЕТСЯ ЛИ ВАЛИДНЫМ
class IsExistsYellowLeafAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, people_id):
        people_list = YellowLeaf.objects.filter(people__id=people_id)
        return Response({"is_exists": len(people_list) > 0}, status=status.HTTP_200_OK)


# ОБНОВЛЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
class UpdateYellowLeafAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, people_id):
        person = YellowLeaf.objects.get(people__id=people_id)
        serializer = YellowLeafFuncSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# РАЗБАН
class RemoveYellowLeafView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, people_id):
        try:
            people_to_ban = YellowLeaf.objects.get(people__id=people_id)
        except Exception:
            return Response({"detail": "Пользователь с указанным id не найден"}, status=status.HTTP_404_NOT_FOUND)

        people_to_ban.delete()
        return Response({"detail": "Пользователь успешно убран из желтого листа"}, status=status.HTTP_200_OK)
