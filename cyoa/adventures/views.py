from django.shortcuts import render
from .models import Question, Choice, Adventure
from django.http import Http404

# Create your views here.
# Used django's tutorials

def index(request):
    """Create page for index: Where all adventures are stored"""
    
    context = {
        'adventures': Adventure.objects.all()
    }
    return render(request, 'adventures/index.html', context)

def adventure(request, adventure_id):
    """Create pages for adventures"""

    # Throw error if adventure doesn't exist
    try:
        adventure = Adventure.objects.get(id=adventure_id)
    except Exception:
        raise Http404("cannot find adventure")

    # go to adventure page, pass adventure to access
    context = {
        'adventure': adventure
    }
    return render(request, 'adventures/adventure.html', context)

def question(request, question_id):
    """Create pages for questions"""

    # error if question doesn't exist
    try:
        question = Question.objects.get(id=question_id)
    except Exception:
        raise Http404("cannot find question")

    # Some questions have input fields, store fields appropriately
    input_field_name = request.GET.get('input_field_name')
    input_field_content = request.GET.get('input_field_content')

    # input fields into game params
    game_params = request.session.setdefault('game_params', {})
    if input_field_name:
        game_params[input_field_name] = input_field_content
        request.session.save()

    # make appropriate changes if text requires it
    question_text = question.question_text
    for name, value in game_params.items():
        question_text = question_text.replace('{' + name + '}', value)

    # allow question content to be accessed
    context = {
        'question': question,
        'question_text': question_text
    }
    return render(request, 'adventures/question.html', context)