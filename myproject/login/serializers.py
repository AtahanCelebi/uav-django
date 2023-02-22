from rest_framework import serializers
from .models import UserRegistration
from django.contrib.auth import authenticate
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username",write_only=True)
    # This will be used when the DRF browsable API is enabled
    password = serializers.CharField(label="Password", style={'input_type': 'password'},trim_whitespace=False,write_only=True)

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs