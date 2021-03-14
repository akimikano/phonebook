from django.contrib import admin

from .models import PhonebookUser, City, Age
from modeltranslation.admin import TabbedTranslationAdmin


class PhonebookUserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'surname', 'phone', 'email', 'age', 'gender', 'work_status', 'city',
              'address', 'status', 'get_in_date', 'get_out_date', 'experience']

    readonly_fields = ['experience']


admin.site.register(PhonebookUser, PhonebookUserAdmin)
admin.site.register(Age)
admin.site.register(City)
