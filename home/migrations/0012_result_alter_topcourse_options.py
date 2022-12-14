# Generated by Django 4.1.1 on 2022-09-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_topcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='images/results/')),
            ],
            options={
                'verbose_name': 'Natijalar',
                'verbose_name_plural': 'Natijalar',
            },
        ),
        migrations.AlterModelOptions(
            name='topcourse',
            options={'verbose_name': 'Top Kurslar', 'verbose_name_plural': 'Top Kurslar'},
        ),
    ]
