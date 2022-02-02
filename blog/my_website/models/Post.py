from django.db import models
from django.core.validators import MinLengthValidator
from .Author import Author
from .Tag import Tag
class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=200)
    # image=models.ImageField(upload_to="posts",null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="Posts")
    tags=models.ManyToManyField(Tag)