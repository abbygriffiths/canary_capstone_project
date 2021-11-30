from django.urls import path

from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.list, name='list_accounts'),
]
