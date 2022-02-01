from django.shortcuts import render,get_object_or_404
from .models import Question
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detailS.html', {'question': question})

def results(request,question_id):
    response="So this is the result of question id %s"%question_id
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse("Voting on question %s." % question_id)