from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('user/<str:username>', views.posts_for_user, name='posts_for_user')
]