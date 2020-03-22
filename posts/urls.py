from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:postid>/upvote/', views.upvote, name='upvote'),
    path('<int:postid>/downvote/', views.downvote, name='downvote'),
    path('postsby/<str:puser>/', views.userposts, name='userposts'),
]