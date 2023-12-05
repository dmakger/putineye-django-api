from rest_framework import serializers

from .models import People, Admin, PeopleToBans, Ban, PeopleToMessage


# ===============
#     PEOPLE
# ===============
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


# ===============
#      ADMIN
# ===============
class AdminSerializer(serializers.ModelSerializer):
    people = PeopleSerializer()

    class Meta:
        model = Admin
        fields = '__all__'


class AdminFuncSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


# ===============
#      BANS
# ===============
class BanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = '__all__'


class PeopleToBanSerializer(serializers.ModelSerializer):
    people = PeopleSerializer()
    ban = BanSerializer()

    class Meta:
        model = PeopleToBans
        fields = '__all__'


class PeopleToBanFuncSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleToBans
        fields = '__all__'


# ===========================
#      PeopleToMessage
# ===========================
class PeopleToMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleToMessage
        fields = '__all__'
