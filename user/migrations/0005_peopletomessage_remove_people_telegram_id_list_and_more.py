# Generated by Django 4.2.7 on 2023-12-04 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_telegramid_people_telegram_id_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleToMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=128, verbose_name='ID чата')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Последнее сообщение пользователя',
                'verbose_name_plural': 'Последние сообщения пользователей',
            },
        ),
        migrations.RemoveField(
            model_name='people',
            name='telegram_id_list',
        ),
        migrations.DeleteModel(
            name='TelegramID',
        ),
        migrations.AddField(
            model_name='peopletomessage',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.people', verbose_name='Пользователь'),
        ),
    ]