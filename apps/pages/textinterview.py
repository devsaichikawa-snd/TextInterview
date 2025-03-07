from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.forms.textinterview_form import TextInterviewInputForm
from apps.views.decorators import log_decorator


@login_required
@log_decorator
def textinterview_top_page(request):
    """TextInterview Top画面"""
    return render(request, "textinterview/textinterview_top.html")


@login_required
@log_decorator
def textinterview_start_page(request):
    """TextInterview Top画面"""
    form = TextInterviewInputForm()
    context = {"form": form}
    return render(request, "textinterview/textinterview_start.html", context)


@login_required
@log_decorator
def textinterview_finish_page(request):
    """TextInterview Top画面"""
    return render(request, "textinterview/textinterview_finish.html")
