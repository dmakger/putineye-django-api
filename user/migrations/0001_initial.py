# Generated by Django 4.2.7 on 2024-01-05 17:11

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
                ('fio', models.CharField(blank=True, max_length=128, null=True, verbose_name='Полное имя')),
                ('telegram_id', models.CharField(max_length=128, verbose_name='ID пользователя в Телеграмме')),
                ('telegram_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя пользователя в Телеграмме')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='YellowLeaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('ban', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.ban', verbose_name='Вид возможного банна')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Желтый список',
                'verbose_name_plural': 'Желтый список',
            },
        ),
        migrations.CreateModel(
            name='PeopleToMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=128, verbose_name='ID чата')),
                ('created_at', models.DateTimeField(verbose_name='Дата последнего сообщения')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Последнее сообщение пользователя',
                'verbose_name_plural': 'Последние сообщения пользователей',
            },
        ),
        migrations.CreateModel(
            name='PeopleToBans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата бана')),
                ('ban', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.ban', verbose_name='Вид банна')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Забаненный пользователь',
                'verbose_name_plural': 'Забаненные пользователи',
            },
        ),
        migrations.CreateModel(
            name='OldDataPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_old', models.CharField(blank=True, max_length=128, null=True, verbose_name='Полное имя')),
                ('telegram_id_old', models.CharField(max_length=128, verbose_name='ID пользователя в Телеграмме')),
                ('telegram_name_old', models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя пользователя в Телеграмме')),
                ('phone_old', models.CharField(blank=True, max_length=128, null=True, verbose_name='Номер телефона')),
                ('created_at_old', models.DateTimeField(verbose_name='Дата регистрации')),
                ('changed_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата смены данных пользователя')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_data_people', to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Старые данные о пользователе',
                'verbose_name_plural': 'Старые данные о пользователе',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата назначения админа')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Админ',
                'verbose_name_plural': 'Админы',
            },
        ),
    ]
