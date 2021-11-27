"""Describe URL patterns for Project Canary website."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('frontend.urls'), name='index'),
    path('accounts/', include('accounts.urls'), name='accounts')
]
