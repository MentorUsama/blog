from django.contrib import admin
from my_website.models.Post import Post
from my_website.models.Author import Author
from my_website.models.Tag import Tag

# Register your models here.
admin.site.register([Post,Author,Tag])