from rest_framework import serializers

from apps.phonebook_app.models import Person


class PersonSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'phone', 'status')

    def get_status(self, obj):
        if obj.status:
            return 'active'
        return 'inactive'


class PersonSerializerDetail(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'phone', 'device', 'address', 'passport', 'status')

    def get_status(self, obj):
        if obj.status:
            return 'active'
        return 'inactive'