# models/AnswerModel.py
from django.db import models
from django.contrib.auth.models import User
from ..models.QuestionModel import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='answer_images/', blank=True, null=True) 
    likes = models.ManyToManyField(User, related_name='answer_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='answer_dislikes', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
