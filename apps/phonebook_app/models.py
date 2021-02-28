from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']

    name = models.CharField('Имя', max_length=20, blank=True, null=True)
    surname = models.CharField('Фамилия', max_length=25, blank=True, null=True)
    phone = PhoneNumberField('Номер телефона')
    passport = models.CharField('Паспорт ID', max_length=9, blank=True, null=True,
                                validators=[RegexValidator(regex='ID\d{7}',
                                                           message='Введите корректный ID',
                                                           code='invalid_passport')])
    address = models.CharField('Адрес', max_length=50, blank=True, null=True)
    device = models.CharField('Устройство', max_length=30, blank=True, null=True)
    status = models.BooleanField('Статус', default=False)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def get_absolute_url(self):
        return reverse('phonebook_detail', kwargs={'pk': self.id})

    def convert_phone(self):
        phone = str(self.phone)
        return '+(996)-{}-{}-{}'.format(phone[4:7], phone[8:11], phone[10:13])
