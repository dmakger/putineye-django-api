from django.db import models


class People(models.Model):
    fio = models.CharField('Полное имя', max_length=128, null=True, blank=True)
    telegram_id = models.CharField('ID пользователя в Телеграмме', max_length=128)

    telegram_name = models.CharField('Имя пользователя в Телеграмме', max_length=128, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=128, null=True, blank=True)
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.get_name()} [{self.phone}]"

    def get_name(self):
        name = self.fio
        if name is None:
            name = self.telegram_name
        if name is None:
            name = self.telegram_id
        return name


class OldDataPeople(models.Model):
    fio_old = models.CharField('Полное имя', max_length=128, null=True, blank=True)
    telegram_id_old = models.CharField('ID пользователя в Телеграмме', max_length=128)

    telegram_name_old = models.CharField('Имя пользователя в Телеграмме', max_length=128, null=True, blank=True)
    phone_old = models.CharField('Номер телефона', max_length=128, null=True, blank=True)
    created_at_old = models.DateTimeField('Дата регистрации')

    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Пользователь',
                               related_name='old_data_people')
    changed_at = models.DateTimeField('Дата смены данных пользователя', auto_now_add=True)

    class Meta:
        verbose_name = "Старые данные о пользователе"
        verbose_name_plural = "Старые данные о пользователе"

    def __str__(self):
        return self.phone_old


class PeopleToMessage(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Пользователь')
    chat = models.CharField('ID чата', max_length=128)
    created_at = models.DateTimeField('Дата последнего сообщения')

    class Meta:
        verbose_name = "Последнее сообщение пользователя"
        verbose_name_plural = "Последние сообщения пользователей"

    def __str__(self):
        return f"{self.people} {self.created_at}"


class Admin(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField('Дата назначения админа', auto_now_add=True)

    class Meta:
        verbose_name = "Админ"
        verbose_name_plural = "Админы"

    def __str__(self):
        return f"{self.people.fio} [{self.people.phone}]"


class Ban(models.Model):
    name = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = "Вид банна"
        verbose_name_plural = "Виды баннов"

    def __str__(self):
        return self.name


class YellowLeaf(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Пользователь')
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE, verbose_name='Вид возможного банна', blank=True, null=True,
                            default=None)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = "Желтый список"
        verbose_name_plural = "Желтый список"

    def __str__(self):
        return f"{self.people.fio} [{self.people.phone}] [{self.ban}]"

    def clean(self):
        if self.ban is None or self.ban == '':
            default_ban_list = Ban.objects.filter(id=3)
            default_ban = None
            if len(default_ban_list) > 0:
                default_ban = default_ban_list[0]
            self.ban = default_ban

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class PeopleToBans(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Пользователь')
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE, verbose_name='Вид банна', blank=True, null=True,
                            default=None)
    created_at = models.DateTimeField('Дата бана', auto_now_add=True)

    class Meta:
        verbose_name = "Забаненный пользователь"
        verbose_name_plural = "Забаненные пользователи"

    def __str__(self):
        return f"{self.people.fio} [{self.people.phone}] [{self.ban}]"

    def clean(self):
        if self.ban is None or self.ban == '':
            default_ban_list = Ban.objects.filter(id=3)
            default_ban = None
            if len(default_ban_list) > 0:
                default_ban = default_ban_list[0]
            self.ban = default_ban

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
