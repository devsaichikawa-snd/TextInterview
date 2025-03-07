from django.shortcuts import render

from apps.views.decorators import log_decorator


@log_decorator
def home_page(request):
    """Home画面View"""
    return render(request, "home.html")
