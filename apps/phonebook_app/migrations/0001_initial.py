# Generated by Django 2.2.5 on 2021-03-13 11:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startswith', models.PositiveIntegerField(verbose_name='От')),
                ('endswith', models.PositiveIntegerField(verbose_name='До')),
            ],
            options={
                'verbose_name': 'Категория возрастов',
                'verbose_name_plural': 'Категории возрастов',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='PhonebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=25, null=True, verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Эл.почта')),
                ('gender', models.SmallIntegerField(choices=[(0, 'Не указано'), (1, 'Мужчина'), (2, 'Женщина')], default=0, verbose_name='Пол')),
                ('work_status', models.SmallIntegerField(blank=True, choices=[(0, 'Стажер'), (1, 'Штатный работник'), (2, 'Уволен')], null=True, verbose_name='Статус работы')),
                ('passport', models.CharField(blank=True, max_length=9, null=True, validators=[django.core.validators.RegexValidator(code='invalid_passport', message='Введите корректный ID', regex='ID\\d{7}')], verbose_name='Паспорт ID')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Адрес')),
                ('device', models.CharField(blank=True, max_length=30, null=True, verbose_name='Устройство')),
                ('status', models.SmallIntegerField(choices=[(0, 'Пользователь'), (1, 'Руководитель'), (2, 'Администратор')], default=0, verbose_name='Статус')),
                ('get_in_date', models.DateField(blank=True, null=True, verbose_name='Дата приема на работу')),
                ('get_out_date', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('experience', models.DateField(blank=True, null=True, verbose_name='Стаж работы')),
                ('age', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='age_person', to='phonebook_app.Age', verbose_name='Категория возрастов')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_person', to='phonebook_app.City', verbose_name='Город')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
