from django.urls import path
from userapplication.views.HomeView import home
from userapplication.views.AskQuestionView import ask_question
from userapplication.views.QuestionDetail import question_detail
from userapplication.views.Like_RepostView import like_answer, dislike_answer, repost_question
from userapplication.views.LoginView import login_view, logout_view
from userapplication.views.RegisterView import register_view


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('ask/', ask_question, name='ask'),
    path('question/<int:question_id>/', question_detail, name='question_detail'),
    path('like/<int:answer_id>/', like_answer, name='like_answer'),
    path('dislike/<int:answer_id>/', dislike_answer, name='dislike_answer'),
    path('repost/<int:question_id>/', repost_question, name='repost_question'),
    
]