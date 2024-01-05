from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Admin, People, PeopleToBans
from user.serializers import AdminSerializer, AdminFuncSerializer


# ВСЕ АДМИНЫ
class AllAdminAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        days = request.data.get('days', None)
        if days is not None:
            days_ago = datetime.now() - timedelta(days=days)
            admins = Admin.objects.filter(created_at__gte=days_ago)
        else:
            admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)


# СОЗДАНИЕ АДМИНА
class AddAdminAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AdminFuncSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        qs = Admin.objects.filter(people__id=request.data.get('people'))
        if len(qs) > 0:
            return Response({'message': 'Такой пользователь уже является админом'}, status=status.HTTP_200_OK)
        serializer.save()

        # Является ли пользователь забаненным
        people_id = serializer.data.get('people')
        user = People.objects.get(pk=people_id)
        # Проверяем, является ли пользователь забаненным
        banned_qs = PeopleToBans.objects.filter(people=user)
        if banned_qs.exists():
            banned_qs.delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ОБНОВЛЕНИЕ ДАННЫХ АДМИНА
class UpdateAdminAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, people_id):
        person = Admin.objects.get(people__id=people_id)
        serializer = AdminFuncSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# УДАЛЕНИЕ АДМИНА
class RemoveAdminView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, people_id):
        qs = Admin.objects.filter(people__id=people_id)
        if len(qs) == 0:
            return Response({"detail": "Админ с указанным пользователем не найден"}, status=status.HTTP_404_NOT_FOUND)

        qs.delete()
        return Response({"detail": "Админ успешно удален"}, status=status.HTTP_200_OK)


# ЯВЛЯЕТСЯ ЛИ ПОЛЬЗОВАТЕЛЬ АДМИНОМ
class IsAdminAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, people_id):
        people_list = Admin.objects.filter(people__id=people_id)
        return Response({"is_admin": len(people_list) > 0}, status=status.HTTP_200_OK)
