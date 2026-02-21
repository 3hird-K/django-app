from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='list'),
    path('<slug:slug>', views.post_detail, name='detail'),
]