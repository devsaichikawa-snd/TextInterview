from django.shortcuts import render

from apps.views.decorators import log_decorator


@log_decorator
def aboutus_page(request):
    """Home画面View"""
    return render(request, "company/about_as.html")
