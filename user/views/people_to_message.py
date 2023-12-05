from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Admin, PeopleToMessage
from user.serializers import PeopleToMessageSerializer


# ДОБАВДЕНИЕ ЗАПИСИ, ЧТО ЧЕЛОВЕК НАПИСАЛ СООБЩЕНИЕ
class AddPeopleToMessageAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PeopleToMessageSerializer(data=request.data)
        print(request.data)
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
