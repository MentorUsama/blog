from django.urls import path
from . import views
app_name = 'my_website'
urlpatterns=[
    path("",views.starting_page.as_view(),name="starting_page"),
    path("posts",views.posts,name="posts-page"),
    path("posts/<slug:slug>",views.post_detail,name="post-detail-page")
]