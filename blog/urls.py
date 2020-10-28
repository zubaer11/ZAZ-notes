from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    #path('blogcomment', views.blog_comment, name = 'blogcomment'),
    path('<str:slug>', views.blog_post, name = 'blogpost'),
]
