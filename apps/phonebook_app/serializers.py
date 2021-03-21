from rest_framework import serializers
from .models import PhonebookUser


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhonebookUser
        fields = ('id', 'name', 'surname', 'phone', 'status')


class PersonSerializerDetail(serializers.Serializer):
    data = PersonSerializer(many=True)


