from rest_framework import serializers

from django.contrib.auth.models import User

from accounts.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'url',)

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = UserProfile
		fields = ('website', 'user', 'url',)

class UsernameSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'url',)