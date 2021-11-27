"""Define the views for the frontend."""

from django.shortcuts import render


def index(request):
    """Index page."""
    context = {'title': 'Index'}
    return render(request, 'frontend/index.html', context)
