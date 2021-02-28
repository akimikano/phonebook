from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.phonebook_app.models import Person
from modeltranslation.admin import TabbedTranslationAdmin


class PersonAdmin(TabbedTranslationAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Person, PersonAdmin)
