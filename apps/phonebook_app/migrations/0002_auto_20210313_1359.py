# Generated by Django 2.2.5 on 2021-03-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonebookuser',
            name='device',
        ),
        migrations.AlterField(
            model_name='phonebookuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='Логин'),
        ),
    ]