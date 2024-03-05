from user.models import Ban


class BanVariables:
    # Бездействие
    INACTION = 4
    # Другая причина
    OTHER = 3
    # Спам
    SPAM = 2
    # Недружественная страна
    UNFRIENDLY_COUNTRY = 1


class BanHelper(BanVariables):

    def __init__(self):
        self._inaction = None
        self._other = None
        self._spam = None
        self._unfriendly_country = None

    # Получение записи типа "Бездействие"
    def inaction(self):
        if self._inaction is None:
            self._inaction = Ban.objects.get(id=self.INACTION)
        return self._inaction

    # Получение записи типа "Другая причина"
    def other(self):
        if self._other is None:
            self._other = Ban.objects.get(id=self.OTHER)
        return self._other

    # Получение записи типа "Спам"
    def spam(self):
        if self._spam is None:
            self._spam = Ban.objects.get(id=self.SPAM)
        return self._spam

    # Получение записи типа "Недружественная страна"
    def unfriendly_country(self):
        if self._unfriendly_country is None:
            self._unfriendly_country = Ban.objects.get(id=self.UNFRIENDLY_COUNTRY)
        return self._unfriendly_country
