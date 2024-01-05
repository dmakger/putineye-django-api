from rest_framework import serializers

from tg.models import Settings


# ===============
#    SETTINGS
# ===============
class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'
