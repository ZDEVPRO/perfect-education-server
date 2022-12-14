# Generated by Django 4.1.1 on 2022-09-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotAndChatId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Bot Token And Chat ID', max_length=600)),
                ('bot_token', models.CharField(max_length=1000)),
                ('chat_id', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'TELEGRAM BOT DATA',
                'verbose_name_plural': 'TELEGRAM BOT DATA',
            },
        ),
    ]
