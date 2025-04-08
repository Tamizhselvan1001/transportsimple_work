from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..forms.AnswerForm import AnswerForm
from ..forms.CommentForm import CommentForm
from ..models.AnswerModel import Answer
from..models.QuestionModel import Question

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.views_count += 1
    question.save()

    answers = question.answers.all()
    answer_form = AnswerForm()
    comment_form = CommentForm()

    if request.method == 'POST':
        if 'answer' in request.POST:
            answer_form = AnswerForm(request.POST, request.FILES)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.user = request.user
                answer.question = question
                answer.save()
                return redirect('question_detail', question_id=question_id)

        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST, request.FILES)
            answer_id = request.POST.get('answer_id')
            answer = get_object_or_404(Answer, id=answer_id)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.answer = answer
                comment.save()
                return redirect('question_detail', question_id=question_id)

    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'answer_form': answer_form,
        'comment_form': comment_form,
    })


