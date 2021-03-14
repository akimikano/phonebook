from rest_framework import serializers
from .models import PhonebookUser


class PersonSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = PhonebookUser
        fields = ('id', 'name', 'surname', 'phone', 'status')

    def get_status(self, obj):
        if obj.status:
            return 'active'
        return 'inactive'


class PersonSerializerDetail(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = PhonebookUser
        fields = ('id', 'name', 'surname', 'phone', 'device', 'address', 'passport', 'status')

    def get_status(self, obj):
        if obj.status:
            return 'active'
        return 'inactive'