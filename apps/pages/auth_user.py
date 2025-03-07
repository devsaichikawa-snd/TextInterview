from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.forms.auth_form import (
    LoginForm,
    SignUpForm,
    ModifyUserInfoForm,
    ResettingPasswordForm,
    DeleteUserForm,
)
from apps.models.auth_model import User
from apps.views.decorators import log_decorator


@log_decorator
def login(request):
    """ログイン画面View"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(
                    request,
                    "ログインしました！",
                )
                return redirect("home")
            else:
                messages.error(
                    request,
                    "メールアドレスまたはパスワードが誤っております。",
                )
        else:
            messages.error(
                request,
                "メールアドレスまたはパスワードが誤っております。",
            )
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "auth/login.html", context)


@login_required
@log_decorator
def logout(request):
    """ログアウト処理"""
    auth_logout(request)
    messages.success(
        request,
        "ログアウトしました！お疲れさまでした！",
    )
    return redirect("login")


@log_decorator
def signup(request):
    """新規登録画面View"""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("user_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            try:
                user = User.objects.create_user(
                    user_name=user_name, email=email, password=password
                )
            except Exception:
                messages.error(
                    request,
                    "登録処理中にエラーが発生しました。",
                )
            else:
                auth_login(request, user)
                messages.success(
                    request,
                    "ユーザー登録が完了しました！ログインしました！早速ご利用いただけます！",
                )
                return redirect("home")
        else:
            messages.error(
                request,
                "入力した内容ではご登録できませんでした。入力内容を見直してください。",
            )
    else:
        form = SignUpForm()

    context = {"form": form}
    return render(request, "auth/signup.html", context)


@login_required
@log_decorator
def modify_userinfo(request):
    """アカウント情報修正画面"""
    user = request.user
    if request.method == "POST":
        form = ModifyUserInfoForm(request.POST)
        if form.is_valid():
            user_obj = User.objects.get(pk=user.user_id)
            user_obj.email = form.cleaned_data.get("email")
            user_obj.save()
            messages.success(
                request,
                "メールアドレスを修正しました！",
            )
            return redirect("home")
    else:
        form = ModifyUserInfoForm(
            initial={"user_name": user.user_name, "email": user.email}
        )

    context = {"form": form}
    return render(request, "auth/modify_userinfo.html", context)


@login_required
@log_decorator
def resetting_password(request):
    """パスワードの再設定画面"""
    user = request.user
    if request.method == "POST":
        try:
            form = ResettingPasswordForm(user=user, data=request.POST)
        except ValueError:
            messages.error(request, "パスワードが誤っています。")
            return redirect("resetting_password")

        if form.is_valid():
            new_password = form.cleaned_data.get("new_password")
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(
                request, user
            )  # パスワード変更後もセッションを維持
            messages.success(request, "パスワードを更新しました！")
            return redirect("home")
    else:
        form = ResettingPasswordForm(user=user)

    context = {"form": form}
    return render(request, "auth/resetting_password.html", context)


@login_required
@log_decorator
def delete_user(request):
    """ユーザーの退会処理"""
    if request.method == "POST":
        form = DeleteUserForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirmed"]:
            user = request.user
            user.delete()
            logout(request)
            messages.success(
                request,
                "アカウントが削除されました。ご利用ありがとうございました。",
            )
            return redirect("home")
    else:
        form = DeleteUserForm()

    context = {"form": form}

    return render(request, "auth/delete_user.html", context)
