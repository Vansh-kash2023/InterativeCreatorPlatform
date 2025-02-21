from rest_framework import serializers
from challenges.models import Challenge, UserProgress

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'difficulty', 'points', 'category', 'created_by']
        read_only_fields = ['created_by']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'challenge', 'completed', 'completion_date', 'points_earned']
        read_only_fields = ['user', 'points_earned']