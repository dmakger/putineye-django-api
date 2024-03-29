from rest_framework import serializers

from .models import People, Admin, PeopleToBans, Ban, PeopleToMessage, YellowLeaf


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
    telegram_id = serializers.SerializerMethodField()

    class Meta:
        model = PeopleToBans
        fields = '__all__'

    def get_telegram_id(self, instance):
        return instance.people.telegram_id


# ===========================
#      PeopleToMessage
# ===========================
class PeopleToMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleToMessage
        fields = '__all__'


# ===========================
#        YellowLeaf
# ===========================
class YellowLeafSerializer(serializers.ModelSerializer):
    people = PeopleSerializer()
    ban = BanSerializer()

    class Meta:
        model = YellowLeaf
        fields = '__all__'


class YellowLeafFuncSerializer(serializers.ModelSerializer):
    class Meta:
        model = YellowLeaf
        fields = '__all__'
