from django.urls import path
from . import views

app_name = 'Tweets'

urlpatterns = [
    path('post/', views.post_tweet, name='post_tweet'),
    path('', views.home, name='home'),
]