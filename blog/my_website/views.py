from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from my_website.models.Post import Post

# Create your views here.
class starting_page(ListView):
    template_name="my_website/index.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"
    def get_queryset(self):
        querySet=super().get_queryset()
        data=querySet[:3]
        return data

def posts(request):
    return HttpResponse("This is posts page")

def post_detail(request,slug):
    return HttpResponse(f"This is post detail page for slug: {slug}")