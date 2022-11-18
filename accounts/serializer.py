from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email',
                    'phone', 'gender', 'user_type', 'is_active', 'is_staff', 
                    'is_superuser' ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for atr, val in validated_data:
            if atr == 'password':
                instance.set_password(val)
            else:
                setattr(atr, val, instance)
        instance.save()
        return instance