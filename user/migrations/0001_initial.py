# Generated by Django 4.2.7 on 2023-12-03 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид банна',
                'verbose_name_plural': 'Виды баннов',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=128, verbose_name='Полное имя')),
                ('phone', models.CharField(max_length=128, verbose_name='Номер телефона')),
                ('telegram_id', models.CharField(max_length=128, verbose_name='ID пользователя в Телеграмме')),
                ('telegram_name', models.CharField(max_length=128, verbose_name='Имя пользователя в Телеграмме')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='PeopleToBans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('ban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ban', verbose_name='Вид банна')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вид банна',
                'verbose_name_plural': 'Виды баннов',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Админ',
                'verbose_name_plural': 'Админы',
            },
        ),
    ]
