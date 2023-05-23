from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        read_only_fields = ("id",)

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.pop('password2', None)
        if password1 != password2:
            raise ValidationError(_("Passwords didn't match."))
        return super().validate(attrs)

    def create(self, validated_data):
        password1 = validated_data.pop('password1', None)
        user = User(**validated_data)
        user.set_password(password1)
        user.save()
        return user


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(email=self.validated_data['email'], date_of_birth=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value


class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')
        model = User.objects.all()
        if username_or_email and password:
            user = authenticate(email=username_or_email, password=password)
            if user:
                attrs['user'] = user
                return attrs

        if username_or_email and password:
            email = model.all().filter(username__exact=username_or_email).values('email').first().get('email')
            user = authenticate(email=email, password=password)
            if user:
                attrs['user'] = user
                return attrs

            else:
                msg = 'avval royxatdan o\'t'
                raise serializers.ValidationError(msg, code='authorization')


class SendEmailVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CheckEmailVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(min_length=6, max_length=6)
