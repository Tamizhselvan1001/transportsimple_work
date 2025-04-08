from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.AnswerModel import Answer
from..models.QuestionModel import Question
from django.contrib.auth.models import User


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answer.likes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)

@login_required
def dislike_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answer.dislikes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)

@login_required
def repost_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.repost_count += 1
    question.save()
    return redirect('question_detail', question_id=question_id)
