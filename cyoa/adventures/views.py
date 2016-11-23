from django.shortcuts import render
from .models import Question, Choice, Adventure
from django.http import Http404

# Create your views here.

def index(request):
    context = {
        'adventures': Adventure.objects.all()
    }
    return render(request, 'adventures/index.html', context)

def adventure(request, adventure_id):
    try:
        adventure = Adventure.objects.get(id=adventure_id)
    except Exception:
        raise Http404("cannot find adventure")

    context = {
        'adventure': adventure
    }
    return render(request, 'adventures/adventure.html', context)

def question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Exception:
        raise Http404("cannot find question")

    input_field_name = request.GET.get('input_field_name')
    input_field_content = request.GET.get('input_field_content')

    game_params = request.session.setdefault('game_params', {})
    if input_field_name:
        game_params[input_field_name] = input_field_content

    question_text = question.question_text
    for name, value in game_params.items():
        question_text = question_text.replace('{' + name + '}', value)

    context = {
        'question': question,
        'question_text': question_text
    }
    return render(request, 'adventures/question.html', context)