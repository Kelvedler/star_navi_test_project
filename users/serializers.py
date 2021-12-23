from rest_framework import serializers
from django.db import transaction
from . import models, jwt


class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        def select_fields(serializer, serializer_fields):
            if isinstance(serializer, serializers.ListSerializer):
                existing = set(serializer.child.fields.keys())
            else:
                existing = set(serializer.fields.keys())
            allowed = set()
            nested_objects = []
            for field, nested_field in serializer_fields.items():
                if nested_field is not None:
                    allowed.add(field)
                    nested_objects.append({field: nested_field})
                else:
                    allowed.add(field)
            if isinstance(serializer, serializers.ListSerializer):
                for field_name in existing - allowed:
                    serializer.child.fields.pop(field_name)
            else:
                for field_name in existing - allowed:
                    serializer.fields.pop(field_name)
            if nested_objects:
                for obj in nested_objects:
                    (name, serializer_fields), = obj.items()
                    if isinstance(serializer, serializers.ListSerializer):
                        select_fields(serializer.child.fields[name], serializer_fields)
                    else:
                        select_fields(serializer.fields[name], serializer_fields)

        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields:
            select_fields(self, fields)


class UserSerializer(DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            user = models.User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
            )
            tokens = jwt.get_tokens_for_user(user)
            user.refresh = tokens['refresh']
            user.access = tokens['access']
        return user
