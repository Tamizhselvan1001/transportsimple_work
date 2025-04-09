from django.urls import path
from .views import (
    QuestionListCreateAPIView,
    QuestionDetailAPIView,
    AnswerCreateAPIView,
    CommentCreateAPIView,
    LikeAnswerAPIView,
    DislikeAnswerAPIView,
    RepostQuestionAPIView
)

urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='api_questions'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='api_question_detail'),
    path('answers/', AnswerCreateAPIView.as_view(), name='api_create_answer'),
    path('comments/', CommentCreateAPIView.as_view(), name='api_create_comment'),
    path('answers/<int:answer_id>/like/', LikeAnswerAPIView.as_view(), name='api_like_answer'),
    path('answers/<int:answer_id>/dislike/', DislikeAnswerAPIView.as_view(), name='api_dislike_answer'),
    path('questions/<int:question_id>/repost/', RepostQuestionAPIView.as_view(), name='api_repost_question'),
]
