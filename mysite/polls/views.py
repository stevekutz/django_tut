from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the results of question %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404 (Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay question voting form
        return render(request, 'polls/detail.html',
            {
                'question': question,
                'error_message': "you did not make a choice",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Return HttpResponseRedirect after a successful POST to prevent
        # data from being posted twice if user hits Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
