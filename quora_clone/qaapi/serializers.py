from rest_framework import serializers
from django.contrib.auth.models import User
from userapplication.models.AnswerModel import Answer
from userapplication.models.QuestionModel import Question
from userapplication.models.CommentModel import Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all().filter(is_active=True))

    class Meta:
        model = Answer
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all().filter(is_active=True))

    class Meta:
        model = Comment
        fields = '__all__'
