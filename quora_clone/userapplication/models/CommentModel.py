# models/CommentModel.py
from django.db import models
from django.contrib.auth.models import User
from ..models.AnswerModel import Answer

class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
