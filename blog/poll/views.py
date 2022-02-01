from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    response="You are looking at question %s."%question_id
    return HttpResponse(response)

def results(request,question_id):
    response="So this is the result of question id %s"%question_id
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse("Voting on question %s." % question_id)