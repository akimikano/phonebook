from modeltranslation.translator import register, TranslationOptions
from apps.phonebook_app.models import Person


@register(Person)
class PersonTO(TranslationOptions):
    fields = ('name', 'surname', 'address', 'device')