# Generated by Django 4.2.7 on 2024-01-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='ban_text',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='link_text',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='welcome_text',
        ),
        migrations.AddField(
            model_name='settings',
            name='text',
            field=models.TextField(default=1, help_text='Текст который будет отображаться', verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Название'),
            preserve_default=False,
        ),
    ]