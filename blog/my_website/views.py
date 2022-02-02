from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_page(request):
    return HttpResponse("This is Starting Page")

def posts(request):
    return HttpResponse("This is posts page")

def post_detail(request,slug):
    return HttpResponse(f"This is post detail page for slug: {slug}")