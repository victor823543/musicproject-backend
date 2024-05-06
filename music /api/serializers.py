from django.contrib.auth.models import User
from api.models import SongStorage, UserStats, UserProgress
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

class SongStorageSerializers(serializers.ModelSerializer):
    class Meta:
        model = SongStorage
        fields = ['id', 'created', 'song', 'title']
    
class UserStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserStats
        fields = ['type', 'sessionStats', 'progressStats']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserProgress
        fields = ['intervalProgress', 'melodyProgress', 'chordProgress', 'progressionProgress']