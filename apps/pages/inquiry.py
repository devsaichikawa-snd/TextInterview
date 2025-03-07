import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.forms.inquiry_form import InquiryForm
from apps.models.inquiry_model import Inquiry
from apps.views.decorators import log_decorator
from common.const import INQUIRY_TYPE_DICT
from common.create_text import create_email_body
from common.email import send_email


@login_required
@log_decorator
def inquiry_top(request):
    """問い合わせフォーム画面"""
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            user = request.user
            input_user_name = form.cleaned_data["user_name"]
            input_email = form.cleaned_data["email"]
            input_inquiry_type = form.cleaned_data["inquiry_type"]
            input_subject = form.cleaned_data["subject"]
            input_message_body = form.cleaned_data["message_body"]
            sending_inquery_type = INQUIRY_TYPE_DICT[input_inquiry_type]
            sending_subject = (
                f"【TextInterview】【問い合わせ】:{input_subject}"
            )
            sending_body = create_email_body(
                input_user_name,
                input_email,
                sending_inquery_type,
                input_message_body,
            )
            try:
                send_email(
                    sending_subject,  # 件名
                    sending_body,  # 本文
                    input_email,  # From
                    [os.getenv("INQUIRY_TO_EMAIL")],  # To
                )
            except Exception as e:
                messages.error(
                    request,
                    "メール送信中にエラーが発生しました。",
                )
            else:
                try:
                    Inquiry.objects.create(
                        user_id=user.user_id,
                        user_name=input_user_name,
                        email=input_email,
                        inquiry_type=input_inquiry_type,
                        subject=input_subject,
                        message_body=input_message_body,
                    )
                except Exception as e:
                    messages.error(
                        request,
                        "登録処理中にエラーが発生しました。",
                    )
                else:
                    messages.success(
                        request, "お問い合わせ内容が送信されました。"
                    )
                    return redirect("home")
        else:
            messages.error(
                request,
                "入力した内容に不備がある為、送信できませんでした。入力内容を見直してください。",
            )
    else:
        form = InquiryForm()

    context = {"form": form}

    return render(request, "company/inquiry_top.html", context)
