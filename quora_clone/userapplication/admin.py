from django.contrib import admin
from .models.AnswerModel import Answer
from .models.QuestionModel import Question
from .models.CommentModel import Comment

class AnswerAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = [
        k.name for k in Answer._meta.fields
    ] 

class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = [
        k.name for k in Question._meta.fields
    ] 
    
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = [
        k.name for k in Comment._meta.fields
    ]     
    
    
admin.site.register(Answer,AnswerAdmin) 
admin.site.register(Question,QuestionAdmin)    
admin.site.register(Comment,CommentAdmin)       