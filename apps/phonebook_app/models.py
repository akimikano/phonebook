from datetime import datetime

from django.contrib.auth import password_validation
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager

WORK_STATUS = [
    (0, 'Стажер'),
    (1, 'Штатный работник'),
    (2, 'Уволен')
]

GENDER = [
    (0, 'Не указано'),
    (1, 'Мужчина'),
    (2, 'Женщина')
]

STATUS = [
    (0, 'Пользователь'),
    (1, 'Руководитель'),
    (2, 'Администратор')
]


class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name


class Age(models.Model):
    class Meta:
        verbose_name = 'Категория возрастов'
        verbose_name_plural = 'Категории возрастов'

    startswith = models.PositiveIntegerField('От')
    endswith = models.PositiveIntegerField('До')

    def __str__(self):
        return '{}-{}'.format(self.startswith, self.endswith)


class PhonebookUserManager(BaseUserManager):
    def _create_user(self, username, name, surname, phone, email, age, gender, work_status,
                     city, address, password, status, **extra_fields):
        if not username:
            raise ValueError('Это поле обязательно')
        username = self.model.normalize_username(username)
        name = name
        surname = surname
        phone = phone
        email = email
        age = age
        gender = gender
        work_status = work_status
        city = city
        address = address
        status = status
        user = self.model(username=username, status=status, name=name, surname=surname, phone=phone,
                          email=email, age=age, gender=gender, work_status=work_status,
                          city=city, address=address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, name, surname, phone, email, age, gender, work_status,
                    city, address, password=None, status=0, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, name, surname, phone, email, age, gender, work_status,
                                 city, address, password, status, **extra_fields)

    def create_superuser(self, username, password, email, status=2, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, email, status, **extra_fields)


class PhonebookUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']

    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "Такой пользователь уже существует.",
        },
    )
    name = models.CharField('Имя', max_length=20, blank=True, null=True)
    surname = models.CharField('Фамилия', max_length=25, blank=True, null=True)
    phone = PhoneNumberField('Номер телефона', error_messages={'invalid': 'Введите номер в формате +996ХХХХХХХХХ'})
    email = models.EmailField('Почта', blank=True, null=True, error_messages={'invalid': 'Введите корректную почту'})
    age = models.ForeignKey(Age, verbose_name='Категория возрастов', related_name='age_person',
                            on_delete=models.CASCADE, blank=True, null=True)
    gender = models.SmallIntegerField('Пол', choices=GENDER, default=0)
    work_status = models.SmallIntegerField('Статус работы', choices=WORK_STATUS, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город', related_name='city_person',
                             on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField('Адрес', max_length=50, blank=True, null=True)
    status = models.SmallIntegerField('Статус', choices=STATUS, blank=True, null=True, default=0)
    get_in_date = models.DateField('Дата приема на работу', blank=True, null=True)
    get_out_date = models.DateField('Дата увольнения', blank=True, null=True)
    experience = models.CharField('Стаж работы', max_length=255, blank=True, null=True)

    # REQUIRED_FIELDS = ['name', 'surname', 'phone', 'email', 'age', 'gender', 'work_status', 'passport', 'city',
    #                    'address']
    REQUIRED_FIELDS = ['phone', 'email']

    @property
    def full_name(self):
        return '{} {}'.format(self.name, self.surname)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def convert_phone(self):
        phone = str(self.phone)
        return '+(996)-{}-{}-{}'.format(phone[4:7], phone[8:11], phone[10:13])

    def save(self, *args, **kwargs):
        if self.get_out_date is not None:
            self.experience = str((self.get_out_date.year - self.get_in_date.year) * 12 +
                                  (self.get_out_date.month - self.get_in_date.month)) + ' мес'
        else:
            self.experience = str((datetime.today().year - self.get_in_date.year) * 12 +
                                  (datetime.today().month - self.get_in_date.month)) + ' мес'
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None



