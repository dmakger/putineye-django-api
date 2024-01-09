# Россия, Казахстан, Беларусь, Азербайджан, Aрмения, Крым
from user.models import Ban, Number


# БАНЫ
class BanHelper:
    SUCCESS_START_PHONE = [7, 77, 375, 994, 374, 365]

    def is_validated_user(self, phone_number: str = None):
        if phone_number is None:
            return True

        start_index = 0
        if phone_number[0] == '+':
            start_index = 1
        phone_number = phone_number[start_index:]

        for phone in Number.objects.filter(is_allowed=True):
            start_ph = str(phone.start).strip()
            len_ph = len(start_ph)
            if phone_number[:len_ph] == str(start_ph):
                return True
        return False

    def get_unfriendly_country(self):
        result = Ban.objects.filter(id=1)
        if len(result) == 0:
            return None
        return result[0]

    def get_spam(self):
        result = Ban.objects.filter(id=2)
        if len(result) == 0:
            return None
        return result[0]

    def get_other(self):
        result = Ban.objects.filter(id=3)
        if len(result) == 0:
            return None
        return result[0]
