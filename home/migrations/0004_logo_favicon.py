# Generated by Django 4.1.1 on 2022-09-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_logo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='favicon',
            field=models.ImageField(default='nimadir', upload_to='images/favicon/'),
            preserve_default=False,
        ),
    ]
