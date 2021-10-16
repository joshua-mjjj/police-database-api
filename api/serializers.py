from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# users Serializer
class User_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class Employee_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'
		
#User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

#Register Serializer
class RegisterSerialzer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(
			validated_data['username'],
			validated_data['email'],
			validated_data['password'])

		return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError('Incorrect Credentials')

 # Serializer for password change endpoint.
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)




