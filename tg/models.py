from django.db import models


class Settings(models.Model):
    title = models.CharField("Название", max_length=100)
    text = models.TextField("Текст", help_text="Текст который будет отображаться")

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return f"{self.id} | {self.title}"
