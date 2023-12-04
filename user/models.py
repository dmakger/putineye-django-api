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
        return f"{self.fio} [{self.phone}]"


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
