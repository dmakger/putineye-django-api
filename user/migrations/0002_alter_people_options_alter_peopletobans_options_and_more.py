# Generated by Django 4.2.7 on 2023-12-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='peopletobans',
            options={'verbose_name': 'Забаненный пользователь', 'verbose_name_plural': 'Забаненные пользователи'},
        ),
        migrations.AlterField(
            model_name='people',
            name='fio',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='people',
            name='telegram_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя пользователя в Телеграмме'),
        ),
    ]
