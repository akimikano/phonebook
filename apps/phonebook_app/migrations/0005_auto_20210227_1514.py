# Generated by Django 2.2.5 on 2021-02-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook_app', '0004_auto_20210227_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]