from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from .models import Question, Choice


def index(request: HttpRequest) -> HttpResponse:
    questions = Question.objects.all().order_by('-published_at')[:5]
    return render(request, 'poll/index.html', {'questions': questions})


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request, 'poll/detail.html', {
        'question': question,
        'choices': choices,
    })


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    choice_id = request.POST.get('choice')

    if not choice_id:
        return detail(request, question_id)

    question = get_object_or_404(Question, pk=question_id)

    try:
        choice = question.choice_set.get(pk=choice_id)
    except Choice.DoesNotExist:
        return detail(request, question_id)

    choice.increase_vote_count()
    choice.save()

    return redirect(f'/polls/{question_id}/result')


def result(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request, 'poll/result.html', {
        'question': question,
        'choices': choices,
    })
