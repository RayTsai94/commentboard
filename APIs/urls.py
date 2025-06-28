from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/comments/', views.get_comments, name='get_comments'),
    path('api/comments/post/', views.post_comment, name='post_comment'),
]